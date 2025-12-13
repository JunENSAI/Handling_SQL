/* LAB: DATE & TIME
   Database: Pagila
*/


```sql
-- 1. Current Time
-- Run this to see what Postgres thinks "Now" is.
SELECT CURRENT_DATE, NOW();

-- 2. Date Arithmetic with Intervals
-- Let's find out when a rental was due.
-- Rule: You have 7 days to return a movie.
SELECT 
	rental_date,
	rental_date + INTERVAL '7 days' AS due_date
FROM rental
LIMIT 10;

-- 3. Calculating Duration (Subtraction)
-- How long did customers actually keep the movies?
SELECT 
	rental_date,
	return_date,
	return_date - rental_date AS duration_interval
FROM rental
WHERE return_date IS NOT NULL
LIMIT 10;

-- 4. Age Function
-- A specific Postgres function that formats the difference nicely.
SELECT 
	rental_date,
	AGE(return_date, rental_date) AS duration_pretty
FROM rental
WHERE return_date IS NOT NULL
LIMIT 10;

-- 5. Extracting Parts
-- We want to know which rentals happened in 2005.
SELECT 
	rental_id,
	rental_date,
	EXTRACT(YEAR FROM rental_date) AS rent_year,
	EXTRACT(MONTH FROM rental_date) AS rent_month,
	EXTRACT(DOW FROM rental_date) AS day_of_week -- 0 is Sunday
FROM rental
WHERE EXTRACT(YEAR FROM rental_date) = 2005
LIMIT 10;

-- 6. TO_CHAR (Formatting for Humans)
-- Turning a timestamp into a readable string like "Mon, DD YYYY"
SELECT 
	rental_date,
	TO_CHAR(rental_date, 'Day, DD Month YYYY') AS pretty_date
FROM rental
LIMIT 5;
```