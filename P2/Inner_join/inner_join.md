## 1. The Keys to the Kingdom

To join tables, you need to find the common thread between them.

* **Primary Key (PK):** A unique ID that identifies a row in its own table (e.g., `customer_id` in the `customer` table).

* **Foreign Key (FK):** A column that points to a Primary Key in *another* table (e.g., `customer_id` in the `payment` table).

---

## 2. The Inner Join (The Intersection)

An `INNER JOIN` returns only the rows where there is a match in **BOTH** tables.

* If a Customer exists but has made 0 payments, they will **NOT** appear in the result.

* If a Payment exists (ghost data) but has no matching Customer, it will **NOT** appear.

----

## 3. Syntax
```sql
SELECT 
    customer.first_name, 
    payment.amount
FROM customer
INNER JOIN payment 
    ON customer.customer_id = payment.customer_id;
```
---