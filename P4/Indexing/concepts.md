## 1. What is an Index?

Imagine a phone book.

* **Unindexed (Full Table Scan):** To find "Smith", you must read every single page from A to Z until you find it.

* **Indexed (B-Tree):** You go to the "S" tab, then "Sm", then "Smith". You find it in 3 steps instead of 1000.

---

## 2. B-Tree (Balanced Tree)

This is the default index type. It is excellent for:

* Equality (`=`)

* Ranges (`<`, `>`, `BETWEEN`)

* Sorting (`ORDER BY`)

---

## 3. The Cost of Indexing

"Why not index everything?"

* **Write Penalty:** Every time you `INSERT` or `UPDATE` a row, the database must also update the Index. If you have 10 indexes, one insert = 11 writes.

* **Space:** Indexes take up hard drive space.

---

## 4. EXPLAIN ANALYZE

This is your X-Ray machine. It tells you exactly how the database plans to run your query.

* **Seq Scan:** Bad (usually). It means reading the whole table.

* **Index Scan:** Good. It used the index.

* **Execution Time:** The only metric that really matters.

----

## 5. Syntax
```sql
CREATE INDEX idx_name ON table_name (column_name);
```
---