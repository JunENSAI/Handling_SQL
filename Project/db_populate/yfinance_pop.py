import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine, text


DB_URL = 'postgresql://postgres:db_password@localhost:5432/pagila'
engine = create_engine(DB_URL)

# Our target companies
tickers = {
    'AAPL': {'name': 'Apple Inc.', 'sector': 'Technology'},
    'TSLA': {'name': 'Tesla Inc.', 'sector': 'Automotive'},
    'JPM':  {'name': 'JPMorgan Chase', 'sector': 'Finance'},
    'PFE':  {'name': 'Pfizer Inc.', 'sector': 'Healthcare'}
}

def populate_companies():
    print("--- 1. Populating Companies ---")
    company_list = []
    for ticker, info in tickers.items():
        company_list.append({
            'company_id': ticker,
            'company_name': info['name'],
            'sector': info['sector']
        })
    
    df = pd.DataFrame(company_list)
    # Use 'append' to avoid deleting the table structure we carefully designed
    df.to_sql('companies', engine, if_exists='append', index=False)
    print("Companies inserted.")

def populate_prices():
    print("--- 2. Populating Stock Prices (Last 30 Days) ---")
    
    for ticker in tickers.keys():
        print(f"Fetching data for {ticker}...")
        
        # Download real data
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1mo")
        
        # Clean Data for SQL : yfinance index is the Date. We need it as a column.
        hist = hist.reset_index()
        
        # Select and Rename columns to match our SQL Schema
        df_sql = pd.DataFrame()
        df_sql['company_id'] = ticker
        df_sql['price_date'] = hist['Date']
        df_sql['open_price'] = hist['Open']
        df_sql['close_price'] = hist['Close']
        df_sql['volume'] = hist['Volume']
        
        # Load to DB
        df_sql.to_sql('stock_prices', engine, if_exists='append', index=False)
        print(f"Loaded {len(df_sql)} rows for {ticker}.")

def create_fake_portfolios():
    print("--- 3. Creating Fake Portfolios ---")
    with engine.connect() as conn:
        conn.execute(text("INSERT INTO portfolios (user_name) VALUES ('Alice'), ('Bob'), ('Charlie');"))
        conn.execute(text("INSERT INTO holdings (portfolio_id, company_id, quantity, purchase_price, purchase_date) VALUES (1, 'AAPL', 10, 150.00, '2025-12-01');"))
        conn.execute(text("INSERT INTO holdings (portfolio_id, company_id, quantity, purchase_price, purchase_date) VALUES (2, 'TSLA', 5, 200.00, '2023-01-05');"))
        conn.commit()

if __name__ == "__main__":
    try:
        populate_companies()
        populate_prices()
        create_fake_portfolios()
        print("\n--- DATABASE READY ---")
    except Exception as e:
        print(f"Error: {e}")