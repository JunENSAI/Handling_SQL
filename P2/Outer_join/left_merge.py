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

def find_missing_inventory():
    conn = psycopg2.connect(**DB_CONFIG)
    
    # 1. Get All Films
    print("--- Fetching Films ---")
    df_films = pd.read_sql("SELECT film_id, title FROM film", conn)
    
    # 2. Get All Inventory
    print("--- Fetching Inventory ---")
    df_inv = pd.read_sql("SELECT DISTINCT film_id FROM inventory", conn)
    df_inv['in_stock'] = True
    
    conn.close()
    
    # 3. Left Merge (SQL: LEFT JOIN)
    print("\n--- Merging ---")
    df_merged = pd.merge(df_films, df_inv, on='film_id', how='left')
 
    missing_films = df_merged[df_merged['in_stock'].isna()]
    
    print(f"Total Films: {len(df_films)}")
    print(f"Films NOT in Inventory: {len(missing_films)}")
    print("\n--- Example Missing Films ---")
    print(missing_films['title'].head())

if __name__ == "__main__":
    find_missing_inventory()