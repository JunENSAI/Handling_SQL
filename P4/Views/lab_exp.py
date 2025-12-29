import psycopg2
import time

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def refresh_dashboard():
    conn = psycopg2.connect(**DB_CONFIG)
    conn.autocommit = True # REFRESH commands usually require autocommit or their own transaction
    cur = conn.cursor()
    
    print("--- Starting Nightly Refresh ---")
    start_time = time.time()
    
    try:
        # Imagine we have a heavy view created in SQL
        # cur.execute("REFRESH MATERIALIZED VIEW category_revenue_mat;")
        # print("Refreshed: category_revenue_mat")
        
        time.sleep(1) 
        print("Dashboard views updated successfully.")
        
    except Exception as e:
        print(f"Refresh Failed: {e}")
    
    print(f"Duration: {time.time() - start_time:.2f} seconds")
    
    cur.close()
    conn.close()

if __name__ == "__main__":
    refresh_dashboard()