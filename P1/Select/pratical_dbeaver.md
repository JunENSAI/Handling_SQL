### File 2: Lab Exercises (SQL)
**Filename:** `day_01_lab.sql`

*Instructions: Open DBeaver, connect to the `pagila` database, open a new SQL Script, and copy/paste this code to run it.*

```sql
/* DAY 1 LAB: SELECT FUNDAMENTALS
   Database: Pagila
*/

-- 1. The "Hello World" of SQL
-- Retrieve everything from the actor table.
-- Observation: Look at the columns: actor_id, first_name, last_name, last_update.
SELECT * FROM actor;

-- 2. Projection (Selecting specific columns)
-- We only care about the names, not the IDs or timestamps.
SELECT first_name, last_name 
FROM actor;

-- 3. Handling Duplicates
-- Challenge: Are there duplicate first names in the actor table?
-- Run this first:
SELECT first_name 
FROM actor; 
-- (Check the row count at the bottom of DBeaver)

-- Run this second:
SELECT DISTINCT first_name 
FROM actor;
-- (Did the row count decrease? If so, we had duplicates).

-- 4. Aliasing
-- We can rename columns in the output to make them readable for humans or Python scripts.
SELECT 
	title AS movie_title, 
	rental_rate AS price_per_day,
	replacement_cost AS lost_fee
FROM film
LIMIT 10;

-- 5. Arithmetic in SELECT
-- We can perform math on the fly.
-- Question: If we lost the movie today, what is the difference between replacing it and renting it?
SELECT 
	title, 
	replacement_cost - rental_rate AS cost_difference
FROM film
LIMIT 10;
```