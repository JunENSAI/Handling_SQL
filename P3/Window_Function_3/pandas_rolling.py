import pandas as pd
import psycopg2

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def pandas_rolling():
    conn = psycopg2.connect(**DB_CONFIG)
    query = "SELECT payment_date, amount FROM payment WHERE customer_id = 1 ORDER BY payment_date"
    df = pd.read_sql(query, conn)
    conn.close()
    
    # 1. Running Total (Cumulative Sum)
    df['running_total'] = df['amount'].cumsum()
    
    # 2. Moving Average (Rolling Window)
    # window=3 means (Current + 2 previous)
    df['moving_avg'] = df['amount'].rolling(window=3).mean()
    
    print(df.head(10))

if __name__ == "__main__":
    pandas_rolling()