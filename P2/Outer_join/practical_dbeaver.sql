-- OUTER JOINS : Pagila DB

-- 1. Basic LEFT JOIN
-- Show all Films, and their Inventory IDs.
-- Note: Some films might not be in our inventory (we don't own the DVD).
-- An Inner Join would hide those films. A Left Join reveals them.
SELECT 
    f.film_id,
    f.title,
    i.inventory_id
FROM film f
LEFT JOIN inventory i 
    ON f.film_id = i.film_id
WHERE f.film_id BETWEEN 1 AND 20; 

-- 2. The Anti-Join (Finding Missing Data)
-- CHALLENGE: Which films exist in our database, but are NOT in our inventory?
-- (i.e., We have the movie info, but no physical DVD to rent).
SELECT 
    f.title,
    i.inventory_id
FROM film f
LEFT JOIN inventory i 
    ON f.film_id = i.film_id
WHERE i.inventory_id IS NULL;

-- 3. Counting the Missing
-- How many movies are we missing from inventory?
SELECT COUNT(*) AS missing_films
FROM film f
LEFT JOIN inventory i ON f.film_id = i.film_id
WHERE i.inventory_id IS NULL;

-- 4. Left Join with Aggregation
-- Show all customers and how much they have spent.
-- If we used INNER JOIN, a customer with $0 spend might disappear 
-- (depending on if they exist in the payment table).
SELECT 
    c.first_name,
    c.last_name,
    SUM(p.amount) AS total_spend
FROM customer c
LEFT JOIN payment p 
    ON c.customer_id = p.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_spend ASC;
