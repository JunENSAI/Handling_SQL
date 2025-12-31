# Config

```python
import pandas as pd
from sqlalchemy import create_engine
import io

DB_URL = 'postgresql://postgres:db_password@localhost:5432/pagila'
engine = create_engine(DB_URL)
```


## Question 1

- Create a DataFrame df with columns student_name and grade: `[('Alice', 85), ('Bob', 90)]`.

- Load this directly into a Postgres table named `exam_results`.

```python
d_1 = {
    'student_name': ['Alice', 'Bob'],
    'grade': [85, 90]
    }
df = pd.DataFrame(data=d_1)

df.to_sql(
    'exam_results', 
    engine, 
    if_exists='replace',
    index=False
    )
```

## Question 2

- Create a DataFrame with dirty data: `data = {'name': [' John ', 'Jane', 'Bob '], 'email': ['JOHN@TEST.COM', 'jane@test.com', 'BOB@test.com']}`

- Transform:

    - Strip whitespace from names (Use `.str.strip()`).

    - Lowercase all emails (Use .`str.lower()`).

    - Load the cleaned data into a table `clean_leads`.

```python
d_2 = {
    'name': [' John ', 'Jane', 'Bob '],
    'email': ['JOHN@TEST.COM', 'jane@test.com', 'BOB@test.com']
    }

df = pd.DataFrame(data=d_2)

df['name'] = df['name'].str.strip() 

df['email'] = df['email'].str.lower()

df_clean = df[['name', 'email']].copy()

df_clean.to_sql(
    'clean_leads', 
    engine, 
    if_exists='replace',
    index=False
    )
```

## Question 3

- Create a DataFrame orders with: `{'order_id': [1, 2, 3], 'amount': [100, 500, 50]}`.

- Transform: Create a new column category.

    - If `amount > 200, category = 'High Value'`.

    - Else, `category = 'Standard'`.

- Load into a table `categorized_orders`.

```python
import numpy as np

d_3 = {
    'order_id': [1, 2, 3],
    'amount': [100, 500, 50]
    }

df = pd.DataFrame(data=d_3)

df['category'] = np.where(df['amount'] > 200, 'High Value', 'Standard')

df.to_sql(
    'categorized_orders', 
    engine, 
    if_exists='replace',
    index=False
    )
```
