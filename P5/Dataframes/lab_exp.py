import pandas as pd
from sqlalchemy import create_engine

# 1. Setup Connections
DB_URL = 'postgresql://postgres:db_password@localhost:5432/pagila'
engine = create_engine(DB_URL)

def pandas_etl_workflow():
    print("--- 1. Extract (Read from SQL) ---")
    # We want to analyze Rental Duration vs Rental Rate
    query = """
    SELECT 
        title, 
        rental_duration, 
        rental_rate, 
        rating 
    FROM film 
    WHERE length > 120;
    """
    
    # Pandas handles the connection and fetching automatically
    df = pd.read_sql(query, engine)
    
    print("Data Fetched:")
    print(df.head())
    
    print("\n--- 2. Transform (Modify in Python) ---")
    # Let's create a new metric: "Cost Per Hour"
    df['cost_ratio'] = df['rental_rate'] / df['rental_duration']
    
    df_filtered = df[df['rating'] == 'PG-13'].copy()
    
    print("Transformed Data:")
    print(df_filtered[['title', 'cost_ratio']].head())
    
    print("\n--- 3. Load (Write back to SQL) ---")
    # We will save this analysis to a new table called 'film_analytics_cache'
    
    try:
        df_filtered.to_sql(
            'film_analytics_cache', 
            engine, 
            if_exists='replace',
            index=False
        )
        print("Success: Data written to 'film_analytics_cache'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pandas_etl_workflow()