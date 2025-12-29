## 1. INSERT

* **Basic:** `INSERT INTO table (col1, col2) VALUES (val1, val2);`

* **Bulk:** You can insert multiple rows in one command (much faster).
    * `VALUES (1, 'A'), (2, 'B'), (3, 'C')`

* **Postgres Special (RETURNING):**

    * Usually, when you insert, SQL says "INSERT 0 1" (silent success).

    * In Postgres, you can say `INSERT ... RETURNING id;` to immediately get back the ID of the new row (crucial for Python apps).

---

## 2. UPDATE

* **Syntax:** `UPDATE table SET col = new_val WHERE condition;`

* **Danger:** If you forget the `WHERE` clause, **every single row** in the table gets updated.

* **Safe Mode:** Always run a `SELECT` with your `WHERE` clause first to ensure you are targeting the right rows.

---

## 3. DELETE

* **Syntax:** `DELETE FROM table WHERE condition;`

* **Danger:** Again, forgetting `WHERE` deletes everything.

* **Difference from TRUNCATE:** `DELETE` scans rows one by one (slow, triggers logs). `TRUNCATE` just drops the data pages (fast, hard to recover).

---

## 4. Upsert (Insert on Conflict)

**What if you try to insert a user, but their ID already exists?**

**Syntax:**
```sql
INSERT INTO table (id, name) VALUES (1, 'John')
ON CONFLICT (id) 
DO UPDATE SET name = 'John';
```