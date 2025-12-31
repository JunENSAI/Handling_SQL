## 1. What are they?

Instead of writing a complex Python script to update 5 tables, you write a **Function** inside Postgres and just call it.

* **Pro:** It runs *inside* the database server (Insanely fast, no network lag).

* **Con:** Harder to debug/version control than Python code.

---

## 2. Syntax: PL/pgSQL
Postgres uses a language called **PL/pgSQL** (Procedural Language / Postgres SQL). It adds `IF` statements, `LOOPS`, and `VARIABLES` to standard SQL.

```sql
CREATE OR REPLACE FUNCTION my_function_name(param1 INT) 
RETURNS INT AS $$
DECLARE
    my_var INT; -- Define variables here
BEGIN
    -- Logic goes here
    SELECT count(*) INTO my_var FROM my_table;
    RETURN my_var + param1;
END;
$$ LANGUAGE plpgsql;
```

---

## 3. Function vs Procedure

- `Function:` Used to calculate values. Can be used inside a SELECT statement. (e.g., SELECT my_func(col) FROM table).

- `Procedure:` Used to perform actions (Insert/Update). Called using CALL my_proc(). Can handle Transactions (Commit/Rollback).

---

## 4. Triggers (The Automated Function)

- A `Trigger `listens for an event (INSERT/UPDATE) and fires a function automatically.

- **Use Case**: Automatically updating a last_updated_at timestamp whenever a row changes.

---