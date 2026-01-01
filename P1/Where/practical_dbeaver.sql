-- FILTERING : Pagila DB

-- 1. Exact Match
-- Find all movies rated 'R'.
SELECT title, rating, length
FROM film
WHERE rating = 'R';

-- 2. Range (BETWEEN)
-- Find movies that are between 60 and 90 minutes long.
SELECT title, length
FROM film
WHERE length BETWEEN 60 AND 90;

-- 3. The "IN" List
-- We need movies with specific rental durations (3, 5, or 7 days).
SELECT title, rental_duration
FROM film
WHERE rental_duration IN (3, 5, 7);

-- 4. Pattern Matching (LIKE)
-- Find all actors whose last name starts with 'Joh'.
-- The % means "anything comes after this".
SELECT first_name, last_name
FROM actor
WHERE last_name LIKE 'JOH%';

-- 5. Postgres Special (ILIKE)
-- Find actors with 'Joh' but ignore capitalization (matches 'johnson', 'JOHANSSON').
SELECT first_name, last_name
FROM actor
WHERE last_name ILIKE 'joh%';

-- 6. Handling NULLs
-- Find all addresses where the postal_code is missing.
-- Note: In the Pagila standard dataset, most fields are filled, 
-- but let's check the 'address' table (column: address2 is often empty/null).
SELECT address, address2, district
FROM address
WHERE address2 IS NULL;

-- 7. Combining Logic (Preview for Day 3)
-- Find movies that are 'PG-13' AND cost less than 2.99 to rent.
SELECT title, rating, rental_rate
FROM film
WHERE rating = 'PG-13' 
  AND rental_rate < 2.99;
