# 1. DDL vs DML

* **DML (Manipulation):** `SELECT`, `INSERT`, `UPDATE`, `DELETE`. (Working with the rows inside the cabinet).

* **DDL (Definition):** `CREATE`, `ALTER`, `DROP`, `TRUNCATE`. (Building or destroying the cabinet itself).

---

## 2. Creating a Table
The syntax defines the **Schema** (the blueprint).
```sql
CREATE TABLE table_name (
    column_name_1 data_type constraint,
    column_name_2 data_type constraint,
    ...
);
```

---

## 3. Key Data Types (Recap for Design)

- `SERIAL`: The magic Postgres type. It creates an Integer that auto-increments (1, 2, 3...). Use this for IDs.

- `VARCHAR(n)`: Text with a limit.

- `TEXT`: Text without a limit (Preferred in Postgres).

- `BOOLEAN`: True/False (Default can be set).

- `TIMESTAMP`: Date + Time.

---

## 4. Basic Constraints (The Rules)

- `NOT NULL`: The column cannot be empty.

- `DEFAULT value`: If the user doesn't provide a value, use this.

- `created_at TIMESTAMP DEFAULT NOW()`

## 5. Altering and Dropping

- `ALTER TABLE x ADD COLUMN y`: Adds a new field to an existing table.

- `DROP TABLE x`: Deletes the table and all its data permanently.

- `TRUNCATE TABLE x`: Deletes all data, but keeps the table structure. (Faster than DELETE).

---