
```SQL
-- 1. Email Campaign
SELECT LOWER(email) AS clean_email
FROM customer
ORDER BY email ASC;

-- 2. Content Review
SELECT title, length
FROM film
WHERE rating = 'PG-13' AND length > 180;

-- 3. Lost Payments
SELECT payment_id, amount
FROM payment
WHERE amount = 0.00;

-- 4. Late Night Rentals
SELECT rental_id, rental_date
FROM rental
WHERE EXTRACT(HOUR FROM rental_date) >= 22;

-- 5. Replacement Cost
SELECT title, replacement_cost
FROM film
ORDER BY replacement_cost DESC, title ASC
LIMIT 5;

-- 6. The "B" Movies
SELECT title
FROM film
WHERE title LIKE '%Boat%' OR title LIKE '%Beautiful%';

-- 7. Weekend Watch
SELECT rental_id, rental_date
FROM rental
WHERE EXTRACT(DOW FROM rental_date) = 0  
  AND EXTRACT(MONTH FROM rental_date) = 5
  AND EXTRACT(YEAR FROM rental_date) = 2005;

-- 8. Short Description
SELECT 
    'Name: ' || first_name || ' ' || LEFT(last_name, 10) AS formatted_name
FROM actor;

-- 9. Privacy Check
SELECT first_name, last_name, email, active
FROM customer
WHERE active = 0 OR email IS NULL;

-- 10. The New Classics
SELECT title, release_year, rental_rate, rating
FROM film
WHERE release_year = 2006
  AND rental_rate < 1.50
  AND (rating = 'G' OR rating = 'PG');

```