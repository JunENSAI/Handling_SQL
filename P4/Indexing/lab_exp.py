import psycopg2
import time

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def benchmark_query():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    query = "SELECT * FROM payment WHERE amount = 2.99;"
    
    # Run 1: Without Index (assuming we dropped it)
    start = time.time()
    for _ in range(100):
        cur.execute(query)
    end = time.time()
    print(f"Time for 100 queries: {end - start:.4f} seconds")
    
    # Note: On small datasets like Pagila (16k rows), the difference is small (milliseconds).
    # On 1M+ rows, it's seconds vs minutes.
    
    cur.close()
    conn.close()

if __name__ == "__main__":
    benchmark_query()