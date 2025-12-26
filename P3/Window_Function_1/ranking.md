## 1. The Syntax: OVER()

The keyword that triggers a window function is `OVER()`.

It tells SQL: "Don't collapse the rows. Just look *over* a specific set of rows to calculate this value."

---

## 2. PARTITION BY

Think of this like `GROUP BY`, but it happens inside the column.

* `PARTITION BY category_id`: "Restart the counter/calculation every time the category changes."

* If you omit it, the "Window" is the entire table.

---

## 3. The Ranking Functions

Imagine a race.

1.  **ROW_NUMBER():** Unique ID for every row. (1, 2, 3, 4).

    * *Tie-breaker:* If two people tie, the DB arbitrarily picks who is 1 and who is 2.

2.  **RANK():** Standard competition ranking (1, 2, 2, 4).

    * *Note:* It skips numbers after a tie (No 3rd place).

3.  **DENSE_RANK():** No gaps (1, 2, 2, 3).

    * *Note:* "Dense" means the numbers are packed tightly.

---

## 4. Syntax Example
```sql
SELECT 
    title,
    rating,
    length,
    RANK() OVER (PARTITION BY rating ORDER BY length DESC) as rank_in_category
FROM film;
```