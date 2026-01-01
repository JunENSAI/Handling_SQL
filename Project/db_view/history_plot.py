import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

DB_URL = 'postgresql://postgres:db_password@localhost:5432/pagila'
engine = create_engine(DB_URL)

def plot_stock_history(ticker):
    print(f"--- Generating Chart for {ticker} ---")

    query = f"""
    SELECT price_date, close_price 
    FROM stock_prices 
    WHERE company_id = '{ticker}' 
    ORDER BY price_date ASC;
    """

    df = pd.read_sql(query, engine)

    if df.empty:
        print("No data found!")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(df['price_date'], df['close_price'], label=f'{ticker} Price', color='blue')
    plt.title(f'{ticker} Stock History')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.grid(True)

    plt.savefig(f"{ticker}_chart.png")
    print(f"Chart saved as {ticker}_chart.png")

if __name__ == "__main__":
    plot_stock_history('AAPL')