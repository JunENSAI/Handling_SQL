## 1. What is SQLAlchemy?

It is a toolkit that sits between Python and SQL. It has two layers:

1.  **Core (The Engine):** Manages connections efficiently. Instead of opening a new connection for every query (slow), it keeps a "pool" of connections open and reuses them.

2.  **ORM (Object Relational Mapper):** A way to write SQL using *only* Python classes and objects, without writing raw SQL strings.

---

## 2. The Engine Connection
In Dataframes, we used `pd.read_sql(query, engine)`.

We can also use the engine directly to run commands.

```python
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM actor"))
    for row in result:
        print(row)
```
*Note: We `import text from sqlalchemy` to safely handle SQL strings.*

---

## 3. Intro to ORM (Object Relational Mapping)

Imagine never writing `CREATE TABLE or INSERT` again.

- **SQL:** `INSERT INTO users (name) VALUES ('John')`

- **ORM:** 
```python 
user = User(name='John') session.add(user) session.commit()
```

The ORM translates Python Objects into SQL rows automatically.

---