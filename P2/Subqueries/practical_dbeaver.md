`SUBQUERIES`

**Database: Pagila**

```SQL
-- 1. Scalar Subquery (The "Average" Comparison)
-- Task: Find the average length (Run this alone first to see the number)
-- Find all films longer than average."
SELECT 
    title, 
    length 
FROM film
WHERE length > (SELECT AVG(length) FROM film)
ORDER BY length DESC;

-- 2. List Subquery (Using IN)
-- "Find all films that have been returned between specific dates."

SELECT title
FROM film
WHERE film_id IN (
    SELECT inventory.film_id
    FROM inventory
    JOIN rental ON inventory.inventory_id = rental.inventory_id
    WHERE rental.return_date BETWEEN '2005-05-25' AND '2005-05-26'
);

-- 3. Subquery in FROM (Derived Table)
-- "What is the average total spend per customer?"
-- Logic: 
--    1. Calculate SUM(amount) for each customer (Inner Query).
--    2. Calculate AVG() of those sums (Outer Query).

SELECT AVG(total_spend) AS average_lifetime_value
FROM (
    -- Inner Query: The derived table
    SELECT customer_id, SUM(amount) AS total_spend
    FROM payment
    GROUP BY customer_id
) AS customer_totals; -- <--- You MUST alias subqueries in FROM

-- 4. Difference from Average
-- "Show me every film, its length, and how much longer/shorter it is than the average."
SELECT 
    title,
    length,
    length - (SELECT AVG(length) FROM film) AS diff_from_avg
FROM film
LIMIT 10;
```