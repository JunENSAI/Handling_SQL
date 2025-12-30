import psycopg2

# Configuration
DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def safe_search_demo():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    # --- SCENARIO 1: Safe Select ---
    # Imagine this input came from a website search bar
    search_term = "Petals" 
    
    print(f"--- Searching for films containing: {search_term} ---")
    
    sql = "SELECT title, release_year FROM film WHERE title LIKE %s LIMIT 5;"
    
    # We wrap the input in %...% for the LIKE clause
    safe_input = (f"%{search_term}%", ) 
    
    cur.execute(sql, safe_input)
    
    results = cur.fetchall()
    for row in results:
        print(row)
        
    # --- SCENARIO 2: Safe Insert ---
    # Inserting a new actor.
    print("\n--- Safe Insert ---")
    
    insert_sql = "INSERT INTO actor (first_name, last_name) VALUES (%s, %s) RETURNING actor_id;"
    actor_data = ("DANIEL", "PYTHON")
    
    cur.execute(insert_sql, actor_data)
    new_id = cur.fetchone()[0]
    print(f"Inserted Actor ID: {new_id}")
    
    conn.commit()
    
    cur.close()
    conn.close()

if __name__ == "__main__":
    safe_search_demo()