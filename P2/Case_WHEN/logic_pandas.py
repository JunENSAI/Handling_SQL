import pandas as pd
import psycopg2
import numpy as np

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def categorization_demo():
    conn = psycopg2.connect(**DB_CONFIG)
    df = pd.read_sql("SELECT title, length, rental_rate FROM film LIMIT 20", conn)
    conn.close()
    
    print("--- Raw Data ---")
    print(df.head())
    
    # 1. The Slow Way (Apply function)
    def label_length(row):
        if row['length'] < 60: return 'Short'
        elif row['length'] < 120: return 'Medium'
        else: return 'Long'
        
    df['category_apply'] = df.apply(label_length, axis=1)
    
    # 2. The Fast Way (Numpy Select)
    conditions = [
        (df['rental_rate'] < 1.00),
        (df['rental_rate'] < 3.00)
    ]
    choices = ['Budget', 'Standard']
    df['price_tier'] = np.select(conditions, choices, default='Premium')
    
    print("\n--- Processed Data ---")
    print(df[['title', 'length', 'category_apply', 'price_tier']].head())

if __name__ == "__main__":
    categorization_demo()