## 1. Primary Key (PK)

* **Rule:** A column (or set of columns) that uniquely identifies a row.

* **Traits:** Automatically implies `UNIQUE` and `NOT NULL`.

* **Best Practice:** Use a meaningless integer (ID) rather than real data (like email) because real data changes.

---

## 2. Foreign Key (FK)

* **Rule:** Links a column in *this* table to the Primary Key of *another* table.

* **Enforcement:**

    * You cannot insert a payment for a `customer_id` that doesn't exist in the `customer` table.

    * You cannot delete a Customer if they still have Payments (unless you use `CASCADE`).

---

## 3. Unique Constraint

* **Rule:** No two rows can have the same value in this column.

* **Use Case:** Emails, Usernames, SSNs.

---

## 4. Check Constraint (The Logic Guard)

* **Rule:** A custom condition that must be true for every row.

* **Example:** `CHECK (price > 0)` or `CHECK (status IN ('active', 'inactive'))`.

---

## 5. Syntax Example
```sql
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18),
    role VARCHAR(10) DEFAULT 'guest'
);
```
---