import psycopg2

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def create_table_script():
    conn = psycopg2.connect(**DB_CONFIG)
    conn.autocommit = True 
    cur = conn.cursor()
    
    table_name = "python_analytics_cache"
    
    print(f"--- Creating Table: {table_name} ---")

    create_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        report_id SERIAL PRIMARY KEY,
        report_name TEXT NOT NULL,
        generated_at TIMESTAMP DEFAULT NOW(),
        row_count INT DEFAULT 0
    );
    """
    
    try:
        cur.execute(create_query)
        print("Success: Table created.")

        cur.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}';")
        columns = cur.fetchall()
        for col in columns:
            print(f" - {col[0]}: {col[1]}")
            
    except Exception as e:
        print(f"Error: {e}")
        
    # Cleanup
    # cur.execute(f"DROP TABLE {table_name}")
    # print("Table dropped.")
    
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_table_script()