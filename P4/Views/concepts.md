## 1. Standard Views

A View does **not** store data. It stores the **query**.

* When you run `SELECT * FROM my_view`, the database actually runs the long, complex query hidden inside it in real-time.

* **Use Case:** Simplifying complex joins for business users.

    * Instead of asking users to join 5 tables to get "Sales", create a view `sales_report`.

---

## 2. Materialized Views (Postgres Special)

A Materialized View **does** store data.

* It runs the query once and saves the result to the hard drive.

* **Pros:** Insanely fast (pre-calculated).

* **Cons:** Data is stale (frozen in time) until you refresh it.

* **Use Case:** Heavy monthly reports or dashboards where "yesterday's data" is fine.

---

## 3. Syntax
* **Creating:**
```sql
CREATE VIEW view_name AS
SELECT ...;
```

* **Materialized:**

```SQL
CREATE MATERIALIZED VIEW view_name AS
SELECT ...;
```

- Refreshing (Materialized Only):
```SQL
REFRESH MATERIALIZED VIEW view_name;
```

---