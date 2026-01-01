-- CTE : Pagila DB

-- 1. The Basics
-- Calculate the average rental rate of films, then find films that cost more than that.
WITH avg_price_cte AS (
    SELECT AVG(rental_rate) AS avg_rate
    FROM film
)
SELECT 
    title, 
    rental_rate
FROM film
CROSS JOIN avg_price_cte 
WHERE rental_rate > avg_price_cte.avg_rate;


-- 2. CTE vs Subquery (The Logic Cleaner)
-- Task: Find customers who have rented more than 30 times.

WITH rental_counts AS (
    SELECT customer_id, COUNT(*) as total_rentals
    FROM rental
    GROUP BY customer_id
)
SELECT 
    c.first_name, 
    c.last_name, 
    rc.total_rentals
FROM customer c
JOIN rental_counts rc 
    ON c.customer_id = rc.customer_id
WHERE rc.total_rentals > 30
ORDER BY rc.total_rentals DESC;


-- 3. Chaining CTEs (Complex Analytics)
-- Task: Find the total revenue of the "Top 5 Categories" of movies.

WITH category_revenue AS (
    -- Step 1: Join tables and sum amount
    SELECT 
        c.name AS category_name,
        SUM(p.amount) AS total_revenue
    FROM category c
    JOIN film_category fc ON c.category_id = fc.category_id
    JOIN inventory i ON fc.film_id = i.film_id
    JOIN rental r ON i.inventory_id = r.inventory_id
    JOIN payment p ON r.rental_id = p.rental_id
    GROUP BY c.name
),
top_5_categories AS (
    -- Step 2: Filter logic (using simple ORDER BY + LIMIT here)
    SELECT * FROM category_revenue
    ORDER BY total_revenue DESC
    LIMIT 5
)
-- Step 3: Final Output
SELECT * FROM top_5_categories;
