import pandas as pd
import psycopg2

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def get_sorted_films(sort_column, sort_direction='ASC'):
    """
    Dynamically sorts films.
    Note: Column names in ORDER BY cannot be passed as simple SQL parameters (%s)
    because the database treats parameters as values (strings), not identifiers.
    We must use Python formatting for columns, but be careful of Injection!
    """
    
    # Whitelist allowed columns to prevent SQL Injection
    allowed_columns = ['title', 'length', 'rental_rate', 'replacement_cost']
    if sort_column not in allowed_columns:
        raise ValueError("Invalid sort column!")

    conn = psycopg2.connect(**DB_CONFIG)
    
    # We construct the query string safely
    query = f"""
    SELECT title, length, rental_rate, replacement_cost
    FROM film
    WHERE length IS NOT NULL
    ORDER BY {sort_column} {sort_direction}
    LIMIT 10;
    """
    
    print(f"Executing: ORDER BY {sort_column} {sort_direction}")
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Test 1: Cheapest rentals
print("--- Cheapest Rentals ---")
print(get_sorted_films('rental_rate', 'ASC'))

# Test 2: Most expensive to replace
print("\n--- Most Expensive to Replace ---")
print(get_sorted_films('replacement_cost', 'DESC'))