`GROUP BY & HAVING`

**Database: Pagila**

```SQL
-- 1. Simple Grouping
-- How many movies do we have for each rating (G, PG, etc.)?
SELECT 
    rating, 
    COUNT(*) AS total_films
FROM film
GROUP BY rating
ORDER BY total_films DESC;


-- 2. The Power of HAVING
-- We want to find our "VIP Customers".
-- VIP = Customers who have spent more than $100 in total.
SELECT 
    customer_id,
    SUM(amount) AS total_spend
FROM payment
GROUP BY customer_id
HAVING SUM(amount) > 100
ORDER BY total_spend DESC;

-- 3. WHERE vs HAVING (The Trap)
-- Scenario: Calculate average rental duration per rating, 
-- BUT only for movies released in 2006. 
-- AND only show ratings where the average is > 4 days.

SELECT 
    rating,
    AVG(rental_duration) AS avg_duration
FROM film
WHERE release_year = 2006
GROUP BY rating 
HAVING AVG(rental_duration) > 4;

-- 4. Business Question
-- Which staff member processed the most money?
SELECT 
    staff_id,
    SUM(amount) AS total_processed
FROM payment
GROUP BY staff_id;
```