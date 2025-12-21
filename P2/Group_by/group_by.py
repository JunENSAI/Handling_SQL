import pandas as pd
import psycopg2

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def analyze_ratings():
    conn = psycopg2.connect(**DB_CONFIG)
    
    query = "SELECT rating, length FROM film;"
    df = pd.read_sql(query, conn)
    conn.close()
    
    print("--- Raw Data (First 5) ---")
    print(df.head())

    print("\n--- Pandas GroupBy ---")
    # 1. Split (groupby) -> 2. Apply (agg) -> 3. Combine
    summary = df.groupby('rating')['length'].agg(['mean', 'count'])
    
    # Sorting
    summary = summary.sort_values(by='mean', ascending=False)
    
    print(summary)
    
    # Python "HAVING" equivalent : Filter the result of the aggregation
    print("\n--- 'HAVING' count > 200 ---")
    print(summary[summary['count'] > 200])

if __name__ == "__main__":
    analyze_ratings()