## 1. The Problem with Subqueries

Subqueries are powerful, but they are hard to read. You have to read the code "inside-out" (start at the deepest parenthesis and work your way out).

* *Example:* "Select X from (Select Y from (Select Z...))"

---

## 2. The Solution: CTEs (The `WITH` Clause)

A CTE (Common Table Expression) creates a **temporary result set** that exists only for that one query.

* Think of it as defining a variable at the top of your code.

* You read the code **Top-to-Bottom**, just like a story or a Python script.

---

## 3. Syntax
```sql
WITH regional_sales AS (
    SELECT region, SUM(amount) as total_sales
    FROM sales
    GROUP BY region
),
top_regions AS (
    SELECT * FROM regional_sales 
    WHERE total_sales > 1000
)
SELECT * FROM top_regions;
```

---

## 4. Why CTEs are Superior

- **Readability:** You give names to your steps (regional_sales, top_regions).

- **Reusability:** You can reference a CTE multiple times in the final SELECT (you can't do that easily with a subquery).

- **Debugging:** You can easily comment out the final SELECT and just do SELECT * FROM regional_sales to check if your intermediate calculation is correct.

---