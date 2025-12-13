import psycopg2
import pandas as pd

# 1. Setup Connection
DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password',
    'host': 'localhost',
    'port': '5432'
}

try:
    conn = psycopg2.connect(**DB_CONFIG)
    
    # 2. Define the Query
    # We use triple quotes """ for multi-line strings
    sql_query = """
    SELECT title, rating, rental_rate 
    FROM film 
    LIMIT 5;
    """
    
    # 3. Method A: The Raw Cursor Way
    print("--- Method A: Raw Cursor ---")
    cur = conn.cursor()
    cur.execute(sql_query)
    rows = cur.fetchall() # Fetches a list of tuples
    for row in rows:
        print(f"Movie: {row[0]}, Rating: {row[1]}, Price: ${row[2]}")
    cur.close()
    
    # 4. Method B: The Pandas Way
    print("\n--- Method B: Pandas DataFrame ---")
    df = pd.read_sql(sql_query, conn)
    print(df)
    
    conn.close()

except Exception as e:
    print(f"Error: {e}")