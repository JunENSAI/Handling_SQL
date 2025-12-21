import pandas as pd
import psycopg2

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def compare_aggregation():
    conn = psycopg2.connect(**DB_CONFIG)
    
    # 1. THE BAD WAY: Loading data, then calculating
    print("--- Loading Raw Data ---")
    df_raw = pd.read_sql("SELECT amount FROM payment", conn)
    
    # Pandas calculation
    py_sum = df_raw['amount'].sum()
    py_avg = df_raw['amount'].mean()
    print(f"Python Calc -> Sum: {py_sum}, Avg: {py_avg:.4f}")
    
    # 2. THE GOOD WAY: Calculating in SQL
    query = "SELECT SUM(amount), AVG(amount) FROM payment;"
    df_agg = pd.read_sql(query, conn)
    
    sql_sum = df_agg.iloc[0, 0]
    sql_avg = df_agg.iloc[0, 1]
    
    print(f"SQL Calc    -> Sum: {sql_sum}, Avg: {sql_avg:.4f}")
    
    conn.close()

if __name__ == "__main__":
    compare_aggregation()