import pandas as pd
import psycopg2
import json

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def json_demo():
    conn = psycopg2.connect(**DB_CONFIG)

    query = """
    SELECT 
        title,
        jsonb_build_object('rating', rating, 'len', length) as meta_data
    FROM film 
    LIMIT 5;
    """
    
    df = pd.read_sql(query, conn)
    conn.close()
    
    print("--- Raw DataFrame ---")
    print(df.head())
    
    print(f"\nType of meta_data column: {type(df.iloc[0]['meta_data'])}")

    df['rating_extracted'] = df['meta_data'].apply(lambda x: x.get('rating'))
    
    print("\n--- Extracted ---")
    print(df[['title', 'rating_extracted']])

if __name__ == "__main__":
    json_demo()