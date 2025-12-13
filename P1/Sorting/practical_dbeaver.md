/* DAY 3 LAB: SORTING & LOGIC
   Database: Pagila
*/

```sql
-- 1. Basic Sorting
-- List the longest movies first.
SELECT title, length
FROM film
ORDER BY length DESC;

-- 2. Multi-Column Sorting
-- Sort by Rating (G, PG, etc.), then by Length (longest to shortest) within that rating.
SELECT title, rating, length
FROM film
ORDER BY rating ASC, length DESC;

-- 3. Simple Logic (AND)
-- Find movies that are 'G' rated AND shorter than 60 minutes.
SELECT title, rating, length
FROM film
WHERE rating = 'G' AND length < 60;

-- 4. The Parentheses Trap (CRITICAL)
-- Scenario: We want movies suitable for kids (G or PG) that are strictly short (< 50 mins).

-- WRONG WAY:
-- The DB reads this as: (Rating is G) OR (Rating is PG AND length < 50).
-- It returns long 'G' movies, which we didn't want.
SELECT title, rating, length
FROM film
WHERE rating = 'G' OR rating = 'PG' AND length < 50;

-- RIGHT WAY:
-- We use parentheses to group the ratings together.
SELECT title, rating, length
FROM film
WHERE (rating = 'G' OR rating = 'PG') 
  AND length < 50;

-- 5. Using NOT
-- Find all films that are NOT rated 'R'.
SELECT title, rating
FROM film
WHERE NOT rating = 'R'; 
-- Alternative: WHERE rating <> 'R';

-- 6. Controlling NULL Sorts
-- Let's look at the address table again. Sort by address2 to bring NULLs to the top.
SELECT address, address2
FROM address
ORDER BY address2 ASC; -- NULLs are at the bottom by default in ASC

-- Now force them to the top
SELECT address, address2
FROM address
ORDER BY address2 ASC NULLS FIRST;
```