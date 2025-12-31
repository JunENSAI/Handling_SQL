# Config

```python
import pandas as pd
from sqlalchemy import create_engine

DB_URL = 'postgresql://postgres:db_password@localhost:5432/pagila'
engine = create_engine(DB_URL)
```

## Question 1

Write a Python script that `uses pd.read_sql to fetch the Top 5 Customers by total spend` (Sum of amount). Print the DataFrame.

```python
def top_customer():
    query = """
    SELECT 
        customer_id, 
        SUM(amount) as total_spend
    FROM payment
    GROUP BY customer_id
    ORDER BY total_spend DESC
    LIMIT 5;
    """

    df = pd.read_sql(query, engine)

    print(df)
```

## Question 2


- Fetch all rows from the `country` table using Pandas.

- In Pandas, create a new column `is_fav` and set it to True if the country is 'France' or 'Italy', else False.

- Filter the DataFrame to show only is_fav countries.

- Print the result.

```python
def country_lab():

    query = """
    SELECT * FROM country;
    """

    df = pd.read_sql(query, engine)

    print(df.head())

    df['is_fav'] = df['country'].isin(['France', 'Italy'])
    df_filtered = df[df['is_fav'] == True].copy()
    print(df_filtered.head())
```


## Question 3

* Create a DataFrame manually in Python:

```Python

data = {'category': ['Sci-Fi', 'Comedy'], 'avg_score': [8.5, 7.2]}
df_manual = pd.DataFrame(data)
```

* Use to_sql to save this to a new table my_genre_scores in Postgres.

* Immediately use read_sql to query that table and print the result to prove it saved.

```python
def save_df_to_sql():
    data = {'category': ['Sci-Fi', 'Comedy'], 'avg_score': [8.5, 7.2]}
    df_manual = pd.DataFrame(data)

    df_manual.to_sql(
        'my_genre_scores', 
        engine, 
        if_exists='replace',
        index=False
        )
    
    query = """SELECT * FROM my_genre_scores;"""
    df = pd.read_sql(quey,engine)
    print(df)
```