## 1. The Concept

A subquery acts as a **dynamic variable**. Instead of hardcoding a number (e.g., `WHERE length > 115`), you write a query to find that number (`WHERE length > (SELECT AVG(length)...)`).

---

## 2. Three Main Types

### A. Scalar Subquery (Returns 1 Value)

* **Result:** A single cell (1 row, 1 column).

* **Usage:** Use it with standard comparison operators (`=`, `>`, `<`).

* *Example:* `SELECT ... WHERE cost > (SELECT AVG(cost) FROM table)`

### B. List Subquery (Returns 1 Column)

* **Result:** A list of values (Multiple rows, 1 column).

* **Usage:** Use it with `IN` or `NOT IN`.

* *Example:* "Find customers who live in 'A' cities."

    * `WHERE city_id IN (SELECT city_id FROM city WHERE city LIKE 'A%')`

### C. Table Subquery (Returns a Table)

* **Result:** Multiple rows and columns.

* **Usage:** Use it in the `FROM` clause. You **must** give it an alias.

* *Example:* `SELECT * FROM (SELECT * FROM table) AS subquery_alias`

---

## 3. Order of Execution

The **Inner Query** (the subquery) usually runs **first**.

1.  DB calculates the average length (e.g., 115.2).

2.  DB replaces the subquery code with `115.2`.

3.  DB runs the Outer Query using that value.

---

## 4. A Warning
Subqueries can be slow if not careful. Avoid "Correlated Subqueries" (where the inner query depends on the outer query row-by-row) unless necessary. We will discuss alternatives (CTEs) on Day 15.