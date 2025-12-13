"""
DAY 0: SYSTEM CHECK
This script verifies that your Python environment is ready for the course.
It checks for necessary libraries and attempts a connection to your new database.
"""

import sys

def print_status(component, status, message=""):
    color = "\033[92m" if status == "OK" else "\033[91m"
    reset = "\033[0m"
    print(f"[{color}{status}{reset}] {component} {message}")

# 1. Check Libraries
libraries = ['pandas', 'psycopg2', 'sqlalchemy']
print("--- 1. Checking Libraries ---")
for lib in libraries:
    try:
        __import__(lib)
        print_status(lib, "OK")
    except ImportError:
        print_status(lib, "FAIL", "-> Run: pip install " + lib + "-binary" if lib == 'psycopg2' else lib)

# 2. Check Database Connection
DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', # CHANGE THIS to your actual Postgres password
    'host': 'localhost',
    'port': '5432'
}

print("\n--- 2. Checking Database Connection ---")
try:
    import psycopg2
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    # Simple query to check if Pagila is loaded correctly
    # We try to select the version of Postgres
    cur.execute("SELECT version();")
    db_version = cur.fetchone()[0]
    print_status("Connection", "OK", f"Connected to: {db_version[:15]}...")
    
    # Check if tables exist (verifying the Restore process)
    cur.execute("SELECT count(*) FROM information_schema.tables WHERE table_schema = 'public';")
    table_count = cur.fetchone()[0]
    
    if table_count > 0:
        print_status("Pagila Data", "OK", f"Found {table_count} tables in the database.")
    else:
        print_status("Pagila Data", "WARNING", "Connected, but found 0 tables. Did you run the SQL restore script?")
        
    cur.close()
    conn.close()

except Exception as e:
    print_status("Connection", "FAIL", f"\nError: {e}")
    print("\nTip: Check if DBeaver is connected, and verify the 'password' variable in this script.")

print("\n--- End of Day 0 Check ---")