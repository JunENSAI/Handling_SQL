# Config

```python
from sqlalchemy import create_engine, text

DB_URL = 'postgresql://postgres:db_password@localhost:5432/pagila'

engine = create_engine(DB_URL, echo=True)
```

## Question 1

Using sqlalchemy,**write a script that connects to Pagila and selects the email of the customer with customer_id = 1.**

```python
def get_email():
    with engine.connect() as connection:
        query = text("SELECT email FROM customer WHERE customer_id = :x")

        result = connection.execute(query, {"x": 1})

        for row in result:
            print(row[0])
```

## Question 2

Write a function `count_films_by_rating(rating)` using SQLAlchemy.

- Pass the rating (e.g., 'PG') as a parameter.

- Execute a query to count how many films have that rating.

- Print the count.

```python
def count_films_by_rating(rating):
    with engine.connect() as connection:
        query = text("SELECT COUNT(*) as number_film_rated FROM film WHERE rating = :x")

        result = connection.execute(query, {"x": rating})

        for row in result:
            print(f"Counting with rating {rating} : {row[0]}")

# count_film_by_rating('PG') -> Counting with rating PG : 194
```

## Question 3

SQLAlchemy can **Inspect** your database to see table names without writing SQL. Inspect Pagila database

```python
from sqlalchemy import inspect

def inspect_db():
    inspector = inspect(engine)
    res_inspect = inspector.get_table_names()
    print(res_inspect)

# ['actor', 'film', 'payment_p2007_02', 'payment_p2007_03', 'payment_p2007_04', 'payment_p2007_05', 'payment_p2007_06', 'payment_p2007_01', 'address', 'category', 'city', 'country', 'customer', 'film_actor', 'film_category', 'inventory', 'language', 'rental', 'staff', 'store', 'payment', 'film_analytics_cache']
```