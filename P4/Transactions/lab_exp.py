import psycopg2

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def transfer_funds(amount):
    conn = psycopg2.connect(**DB_CONFIG)
    # conn.autocommit = False (This is default in psycopg2, so we are already in a transaction block)
    cur = conn.cursor()
    
    print(f"--- Attempting to Transfer ${amount} ---")
    
    try:
        # Assume that you created table my_back from dbeaver_practice
        cur.execute("UPDATE my_bank SET balance = balance - %s WHERE name = 'Alice'", (amount,))
        
        if amount > 500:
            raise Exception("System Crash! Amount too large.")

        cur.execute("UPDATE my_bank SET balance = balance + %s WHERE name = 'Bob'", (amount,))
        
        conn.commit()
        print("Success: Transfer Complete.")
        
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
        print("Transaction Rolled Back. No money lost.")
        
    cur.close()
    conn.close()

if __name__ == "__main__":
    # Test 1: Valid
    transfer_funds(100)
    
    # Test 2: Invalid (Simulating crash)
    transfer_funds(1000)