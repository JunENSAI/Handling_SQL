-- CASE WHEN : Pagila DB

-- 1. Basic Categorization
-- Label movies based on their length.
SELECT 
    title,
    length,
    CASE
        WHEN length < 60 THEN 'Short (< 1h)'
        WHEN length BETWEEN 60 AND 120 THEN 'Medium (1h-2h)'
        WHEN length > 120 THEN 'Long (> 2h)'
        ELSE 'Unknown' -- Good practice to handle nulls
    END AS duration_category
FROM film
LIMIT 15;

-- 2. Categorizing Price (Binning)
-- Let's group rentals into price tiers.
SELECT 
    title,
    rental_rate,
    CASE 
        WHEN rental_rate < 1.00 THEN 'Budget'
        WHEN rental_rate < 3.00 THEN 'Standard'
        ELSE 'Premium'
    END AS price_tier
FROM film
ORDER BY rental_rate DESC
LIMIT 15;

-- 3. Pivot Table with Count (The "Sum-If" Trick)
-- We want one row that shows the count of G, PG, and R movies side-by-side.
-- Regular GROUP BY creates 3 rows. This creates 1 row with 3 columns.
SELECT 
    COUNT(*) AS total_movies,
    SUM(CASE WHEN rating = 'G' THEN 1 ELSE 0 END) AS count_g,
    SUM(CASE WHEN rating = 'PG' THEN 1 ELSE 0 END) AS count_pg,
    SUM(CASE WHEN rating = 'R' THEN 1 ELSE 0 END) AS count_r
FROM film;

-- 4. Updating Data Logic (Active Status)
-- The customer table has an 'active' column (1 or 0). 
SELECT 
    first_name,
    last_name,
    CASE 
        WHEN active = 1 THEN 'Active'
        ELSE 'Inactive'
    END AS status
FROM customer
LIMIT 10;
