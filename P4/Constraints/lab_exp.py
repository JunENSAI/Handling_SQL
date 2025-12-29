import psycopg2
from psycopg2 import IntegrityError

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def test_integrity():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    print("--- Attempting to Insert Duplicate ---")
    
    try:
        sql = "INSERT INTO my_authors (name, email) VALUES ('Python User', 'py@test.com')"
        
        cur.execute(sql)
        cur.execute(sql) # The second time should fail
        
        conn.commit()
    except IntegrityError as e:
        conn.rollback()
        print(f"\n[CAUGHT ERROR]: {e}")
        print("-> The database successfully stopped the duplicate data!")
    
    cur.close()
    conn.close()

if __name__ == "__main__":
    test_integrity()