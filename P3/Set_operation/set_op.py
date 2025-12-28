import pandas as pd
import psycopg2

DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}

def pandas_sets():
    conn = psycopg2.connect(**DB_CONFIG)
    
    # Get two lists
    actors = pd.read_sql("SELECT first_name, last_name FROM actor", conn)
    customers = pd.read_sql("SELECT first_name, last_name FROM customer", conn)
    conn.close()
    
    actor_set = set(zip(actors['first_name'], actors['last_name']))
    customer_set = set(zip(customers['first_name'], customers['last_name']))
    
    # 1. UNION ( | )
    all_people = actor_set | customer_set
    print(f"Total Unique People: {len(all_people)}")
    
    # 2. INTERSECT ( & )
    common_people = actor_set & customer_set
    print(f"People in both lists: {common_people}")
    
    # 3. DIFFERENCE ( - )
    just_actors = actor_set - customer_set
    print(f"Actors who are not customers: {len(just_actors)}")

if __name__ == "__main__":
    pandas_sets();