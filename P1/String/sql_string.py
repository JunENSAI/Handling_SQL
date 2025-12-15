import pandas as pd
import psycopg2

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def clean_emails():
    conn = psycopg2.connect(**DB_CONFIG)
    
    # We fetch the raw emails
    query = "SELECT email FROM customer LIMIT 10;"
    df = pd.read_sql(query, conn)
    conn.close()
    
    print("--- Raw Data ---")
    print(df.head(3))
    
    # Python String Manipulation
    # Logic: Split the string by '@' and take the second part (index 1)
    # Note: In Python, we use apply() or vector functions .str
    
    df['domain'] = df['email'].apply(lambda x: x.split('@')[1])
    
    df['domain_cap'] = df['domain'].str.upper()
    
    print("\n--- Processed in Python ---")
    print(df[['email', 'domain', 'domain_cap']].head())

if __name__ == "__main__":
    clean_emails()