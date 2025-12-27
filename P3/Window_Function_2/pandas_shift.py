import pandas as pd
import psycopg2

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def pandas_shift():
    conn = psycopg2.connect(**DB_CONFIG)
    # Get payments for one specific customer to keep it simple
    query = "SELECT payment_date, amount FROM payment WHERE customer_id = 1 ORDER BY payment_date"
    df = pd.read_sql(query, conn)
    conn.close()
    
    print("--- Raw Data ---")
    print(df.head())
    
    # SQL: LAG(amount, 1)
    # Pandas: df['amount'].shift(1)
    df['prev_amount'] = df['amount'].shift(1)
    
    df['diff'] = df['amount'] - df['prev_amount']
    
    print("\n--- After Shift ---")
    print(df.head())

if __name__ == "__main__":
    pandas_shift()