## 1. Why use Pandas with SQL?

`psycopg2` returns data as a list of tuples: `[(1, 'John'), (2, 'Jane')]`.

* You lose column names.

* You can't easily analyze statistics.

* You can't visualize it.

Pandas solves this. It loads data directly into a structured table (DataFrame).

---

## 2. Reading Data (`read_sql`)

The magic function is `pd.read_sql(query, connection)`.

* It automatically runs the query.

* It fetches all rows.

* It uses the database column names as the DataFrame headers.

```python
df = pd.read_sql("SELECT * FROM payment", conn)
```

---

## 3. Writing Data (to_sql)

Writing data back to SQL is trickier. Pandas requires a SQLAlchemy Engine, not just a raw psycopg2 connection, to handle the heavy lifting of creating INSERT statements automatically.

The setup:

```Python

from sqlalchemy import create_engine
# Format: postgresql://user:password@host:port/dbname
engine = create_engine('postgresql://postgres:password@localhost:5432/pagila')

# Write DataFrame to SQL
df.to_sql('table_name', engine, if_exists='append', index=False)
```
- `if_exists:`

    - 'fail': Stop if table exists.

    - 'replace': Drop table and recreate (Dangerous!).

    - 'append': Add rows to existing table.

---