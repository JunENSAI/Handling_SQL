import pandas as pd
import psycopg2

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def analyze_dtypes():
    conn = psycopg2.connect(**DB_CONFIG)
    
    # We select data with different types
    query = """
    SELECT 
        title,                  -- Text
        release_year,           -- Integer (sometimes Year type)
        rental_rate,            -- Numeric
        last_update             -- Timestamp
    FROM film 
    LIMIT 5;
    """
    
    print("--- Loading Data from SQL ---")
    df = pd.read_sql(query, conn)
    
    # 1. Check how Pandas interpreted the SQL types
    print("\n--- Pandas Data Types ---")
    print(df.dtypes)
    
    # 2. Doing math on the Numeric column
    # Since rental_rate is Numeric in SQL, Pandas usually makes it Float64.
    average_price = df['rental_rate'].mean()
    print(f"\nAverage Price (calculated in Python): ${average_price:.2f}")

    conn.close()

if __name__ == "__main__":
    analyze_dtypes()