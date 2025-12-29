import psycopg2

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def dml_demo():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    # 1. Create a task and get its ID immediately : %s is the placeholder for variables
    sql_insert = "INSERT INTO my_todo (task) VALUES (%s) RETURNING task_id;"
    
    task_name = "Master Python DB"
    cur.execute(sql_insert, (task_name,))
    
    # Fetch the returned ID
    new_id = cur.fetchone()[0]
    print(f"Created Task '{task_name}' with ID: {new_id}")
    
    # 2. Update it using that ID
    sql_update = "UPDATE my_todo SET status = 'done' WHERE task_id = %s;"
    cur.execute(sql_update, (new_id,))
    
    conn.commit() # Don't forget to commit changes!
    conn.close()

if __name__ == "__main__":
    dml_demo()