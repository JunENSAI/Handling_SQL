`RANKING`

**Database: Pagila**

```sql
-- 1. ROW_NUMBER
-- Assign a unique ID to every rental based on the rental date.
SELECT 
    rental_id,
    rental_date,
    ROW_NUMBER() OVER (ORDER BY rental_date ASC) as rental_sequence
FROM rental
LIMIT 10;

-- 2. PARTITION BY
-- "Show me the 1st, 2nd, 3rd movie each specific customer rented."
SELECT 
    customer_id,
    rental_date,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY rental_date ASC) as customer_rental_history
FROM rental
ORDER BY customer_id, rental_date
LIMIT 20;

-- 3. RANK vs DENSE_RANK
-- Let's look at film lengths. Many films have the same length (ties).
SELECT 
    title,
    length,
    RANK() OVER (ORDER BY length DESC) as rank_standard,
    DENSE_RANK() OVER (ORDER BY length DESC) as rank_dense
FROM film
WHERE length > 180
ORDER BY length DESC;
-- Notice: RANK skips numbers (1, 1, 3). DENSE_RANK does not (1, 1, 2).