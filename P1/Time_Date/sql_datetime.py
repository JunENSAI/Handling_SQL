import pandas as pd
import psycopg2

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def analyze_rental_days():
    conn = psycopg2.connect(**DB_CONFIG)
    
    # We extract the Day of Week (0-6) directly from SQL
    query = """
    SELECT 
        rental_id,
        rental_date,
        EXTRACT(DOW FROM rental_date) AS day_index
    FROM rental
    WHERE rental_date BETWEEN '2005-05-01' AND '2005-06-01';
    """
    
    df = pd.read_sql(query, conn)
    conn.close()
    
    # Map the 0-6 index to actual names
    days_map = {
        0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
        4: 'Thursday', 5: 'Friday', 6: 'Saturday'
    }
    
    # create a new column using the map
    df['day_name'] = df['day_index'].map(days_map)
    
    print("--- Sample Data ---")
    print(df[['rental_date', 'day_name']].head())
    
    # Simple analytics: Which day is most popular?
    print("\n--- Rentals per Day ---")
    print(df['day_name'].value_counts())

if __name__ == "__main__":
    analyze_rental_days()