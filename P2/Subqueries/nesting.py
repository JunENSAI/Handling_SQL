import pandas as pd
import psycopg2

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def subquery_demo():
    conn = psycopg2.connect(**DB_CONFIG)
    
    # We want to find customers who spent more than the average customer.
    
    query = """
    SELECT 
        customer_id, 
        SUM(amount) as my_spend
    FROM payment
    GROUP BY customer_id
    HAVING SUM(amount) > (
        SELECT AVG(total_spend)
        FROM (
            SELECT customer_id, SUM(amount) as total_spend
            FROM payment
            GROUP BY customer_id
        ) as sub
    )
    ORDER BY my_spend DESC
    LIMIT 10;
    """
    
    print("--- High Value Customers (Above Average) ---")
    df = pd.read_sql(query, conn)
    print(df)
    
    conn.close()

if __name__ == "__main__":
    subquery_demo()