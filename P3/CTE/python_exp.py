import pandas as pd
import psycopg2

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def cte_demo():
    conn = psycopg2.connect(**DB_CONFIG)
    
    # We want to find "High Value Customers" in specific "Focus Cities".
    
    query = """
    WITH customer_spend AS (
        -- Calculate how much each customer spent
        SELECT customer_id, SUM(amount) as total_spent
        FROM payment
        GROUP BY customer_id
    ),
    focus_cities AS (
        -- We only care about customers in Aurora or Sasebo
        SELECT city_id, city
        FROM city
        WHERE city IN ('Aurora', 'Sasebo')
    )
    SELECT 
        c.first_name,
        c.last_name,
        fc.city,
        cs.total_spent
    FROM customer c
    JOIN customer_spend cs ON c.customer_id = cs.customer_id
    JOIN address a ON c.address_id = a.address_id
    JOIN focus_cities fc ON a.city_id = fc.city_id
    WHERE cs.total_spent > 100;
    """
    
    print("--- Executing CTE Query ---")
    df = pd.read_sql(query, conn)
    print(df)
    
    conn.close()

if __name__ == "__main__":
    cte_demo()