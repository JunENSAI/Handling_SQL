import pandas as pd
import psycopg2

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def get_movies_by_rating(rating_input):
    """
    Fetches movies based on a rating provided by the user.
    Uses Parameterized Queries to prevent security issues.
    """
    conn = psycopg2.connect(**DB_CONFIG)
    
    # query uses %s as a placeholder for the variable
    query = """
    SELECT title, rating, release_year
    FROM film
    WHERE rating = %s
    LIMIT 10;
    """

    df = pd.read_sql(query, conn, params=(rating_input,))
    
    conn.close()
    return df

# Run the function
user_rating = 'NC-17'
print(f"--- Top 10 movies rated {user_rating} ---")
results = get_movies_by_rating(user_rating)
print(results)