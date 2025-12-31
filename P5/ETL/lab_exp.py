import pandas as pd
from sqlalchemy import create_engine
import io

DB_URL = 'postgresql://postgres:db_password@localhost:5432/pagila'
engine = create_engine(DB_URL)

def run_etl_pipeline():
    print("--- 1. Extract (Simulating CSV read) ---")

    csv_data = """id,product_name,raw_price,sale_date
    101,Super Widget,$50.00,2023-01-01
    102,Mega Widget,NaN,2023-01-02
    103,Old Widget,$10.00,invalid-date
    """
    df = pd.read_csv(io.StringIO(csv_data))
    print("Raw Data:")
    print(df)

    print("\n--- 2. Transform ---")

    df['price'] = df['raw_price'].str.replace('$', '').astype(float)
    
    avg_price = df['price'].mean()
    df['price'] = df['price'].fillna(avg_price)
    
    df['clean_date'] = pd.to_datetime(df['sale_date'], errors='coerce')
    
    df_clean = df[['id', 'product_name', 'price', 'clean_date']].copy()
    
    print("Clean Data:")
    print(df_clean)

    print("\n--- 3. Load ---")
    try:
        df_clean.to_sql(
            'daily_sales_report', 
            engine, 
            if_exists='replace',
            index=False
        )
        print("Success: Pipeline Finished.")
    except Exception as e:
        print(f"ETL Failed: {e}")

if __name__ == "__main__":
    run_etl_pipeline()