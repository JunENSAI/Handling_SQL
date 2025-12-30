# Config 

```python
import psycopg2

# Configuration
DB_CONFIG = {
    'dbname': 'pagila',
    'user': 'postgres',
    'password': 'db_password', 
    'host': 'localhost',
    'port': '5432'
}
```

## Question 01 : 

Write a Python function `get_customer_by_email(email)` that connects to Pagila.

Return the customer_id and first_name for that email using a parameterized query.

```python
def get_customer_by_email(email):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    query_sql = "SELECT customer_id, first_name from customer where email = %s;"

    cur.execute(query_sql, (email,))
    results = cur.fetchall()
    print(results)
    
    cur.close()
    conn.close()
```

## Question 2

Write a Python function `add_new_city(city, country_id)` that inserts a new city into the city table.

- **Constraint:** You must use RETURNING city_id to print the ID of the new city.

- **Security:** Ensure city_name and country_id are passed safely.

```python
def add_new_city(city_name, country_id):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    query_sql = "INSERT INTO city (city_name, country_id) VALUES (%s, %s) RETURNING city_id;"

    cur.execute(query_sql, (city_name,country_id))
    new_id = cur.fetchone()[0]
    print(f"Inserted City ID: {new_id}")
    
    conn.commit()
    cur.close()
    conn.close()
```

## Question 3

Write a Python function `update_rental_duration(film_title, new_duration)`.

- Find the film_id by searching for the film_title (Safe Select).

- If the film exists, update its rental_duration to the new_duration (Safe Update).

- If the film does not exist, print "Film not found."

- Important: Handle the case where there are multiple films with the same title (just pick the first one or error out).

```python
def update_rental_duration(film_title, new_duration):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    query_1 = "SELECT film_id from film where title = %s;"

    cur.execute(query_1, (film_title,))

    result = cur.fetchone()

    if result:
        film_id = result[0]
        query_2 = "UPDATE film SET rental_duration = %s WHERE film_id = %s;"
        cur.execute(query_2, (new_duration,film_id))
        conn.commit()
        print(f"Success: Updated film ID {film_id}")
    else:
        print("Film not found")
    cur.close()
    conn.close()
```