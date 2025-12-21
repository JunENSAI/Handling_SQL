## 1. The Concept (Split-Apply-Combine)

`GROUP BY` changes how the database processes data:

1.  **Split:** It cuts the table into "buckets" based on the column you specify (e.g., `rating`).

2.  **Apply:** It runs your aggregate function (SUM, COUNT) on *each bucket individually*.

3.  **Combine:** It returns one result per bucket.

---

## 2. The Golden Rule of GROUP BY

If you use `GROUP BY`, your `SELECT` statement can **only** contain:

1.  The columns you grouped by.

2.  Aggregate functions (`SUM`, `COUNT`, etc.).

* **Error:** `SELECT actor_id, SUM(amount) FROM payment GROUP BY customer_id;`

* **Why:** The DB doesn't know which `actor_id` to show for the group of payments belonging to a `customer_id`.

---

## 3. HAVING vs WHERE

This is the most common interview question.

* **WHERE**: Filters **Rows** *before* they are grouped.

    * *"Include only payments > $5, then group them."*

* **HAVING**: Filters **Groups** *after* the aggregation is done.

    * *"Group all payments by customer, sum them up, then show me only customers who spent > $100."*

---

## 4. Order of Execution (Updated)

1.  `FROM` (Load Table)

2.  `WHERE` (Filter Rows)

3.  **`GROUP BY`** (Make Buckets)

4.  **`HAVING`** (Filter Buckets)

5.  `SELECT` (Return Columns)

6.  `ORDER BY` (Sort)

7.  `LIMIT` (Cut off)

---