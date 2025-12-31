# Config

```python
from sqlalchemy import create_engine
imoprt pandas as pd
import numpy as np

DB_URL = 'postgresql://postgres:db_password@localhost:5432/pagila'
engine = create_engine(DB_URL)
```

## Question 1

```sql
CREATE TABLE hr_employees (
    emp_id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    salary INTEGER CHECK(salary > 0),
    department TEXT,
    is_high_earner BOOLEAN -- let the python script decide for the value because it's after the cleaning salary
);
```

## Question 2

```python
def clean_salary(value: str) -> int:
    value = value.lower().replace('$', '').replace(',', '').replace('/yr', '').strip()

    if 'k' in value:
        return int(float(value.replace('k', '')) * 1000)

    return int(float(value))
```

## Question 3

```python
def etl_process():

    raw_data = {
    'id': [101, 102, 103],
    'name': ['Doe, John', 'Smith, Jane', 'Brown, Bob'],
    'raw_salary': ['$120,000/yr', '85k', ' $45,000 '],
    'dept': ['Engineering', 'Marketing', 'Sales']
    }

    df['salary'] = df['raw_salary'].apply(clean_salary)

    df['full_name'] = df['name'].apply(lambda x: ' '.join(x.split(', ')[::-1]))

    df['is_high_earner'] = np.where(df['salary'] > 100000, True, False)

    df_final = df.rename(columns={'id': 'emp_id', 'dept': 'department'})

    cols_to_load = ['emp_id', 'full_name', 'salary', 'department', 'is_high_earner']
    
    try:
        df_final[cols_to_load].to_sql(
            'hr_employees', 
            engine, 
            if_exists='append',
            index=False
        )
        print("Success: Data written to 'hr_employees'")
    except Exception as e:
        print(f"Error: {e}")
```