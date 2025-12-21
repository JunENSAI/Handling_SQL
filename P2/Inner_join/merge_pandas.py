import pandas as pd
import psycopg2

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def pandas_join():
    conn = psycopg2.connect(**DB_CONFIG)
    
    # 1. Fetch two separate datasets
    print("--- Fetching Tables ---")
    df_cust = pd.read_sql("SELECT customer_id, first_name, last_name FROM customer", conn)
    df_pay = pd.read_sql("SELECT customer_id, amount, payment_date FROM payment", conn)
    
    conn.close()
    
    # 2. Perform the Merge (Inner Join)
    print("\n--- Merging Data ---")
    merged_df = pd.merge(df_cust, df_pay, on='customer_id', how='inner')
    
    print(merged_df[['first_name', 'amount']].head())
    

    print(f"\nRows in Customers: {len(df_cust)}")
    print(f"Rows in Payments: {len(df_pay)}")
    print(f"Rows in Result: {len(merged_df)}") 

if __name__ == "__main__":
    pandas_join()