import pandas as pd
import psycopg2

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def pandas_ranking():
    conn = psycopg2.connect(**DB_CONFIG)
    df = pd.read_sql("SELECT title, length, rating FROM film WHERE length > 170", conn)
    conn.close()
    
    # SQL: RANK() OVER (PARTITION BY rating ORDER BY length DESC)
    # Pandas: groupby(partition)[col].rank(method, ascending)
    
    # method='min' is similar to SQL RANK
    # method='dense' is SQL DENSE_RANK
    # method='first' is SQL ROW_NUMBER
    
    df['rank'] = df.groupby('rating')['length'].rank(method='min', ascending=False)
    
    print(df.sort_values(['rating', 'rank']).head(10))

if __name__ == "__main__":
    pandas_ranking()