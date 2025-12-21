/* INNER JOINS
   Database: Pagila
*/

```sql
-- 1. The Basic Join
-- We want to see the name of the customer alongside their payment amount.
-- (Customer Table) + (Payment Table)
SELECT 
    c.first_name,
    c.last_name,
    p.amount,
    p.payment_date
FROM customer c
INNER JOIN payment p 
    ON c.customer_id = p.customer_id
LIMIT 10;

-- 2. Joining for "Lookup" Data
-- The 'address' table just has a city_id. 
-- We want the actual name of the city.
SELECT 
    a.address,
    c.city
FROM address a
INNER JOIN city c 
    ON a.city_id = c.city_id
LIMIT 10;

-- 3. The 3-Table Join (The Chain)
-- Country -> City -> Address
-- We want to find all addresses in 'France'.
SELECT 
    co.country,
    ci.city,
    a.address
FROM country co
INNER JOIN city ci 
    ON co.country_id = ci.country_id
INNER JOIN address a 
    ON ci.city_id = a.city_id
WHERE co.country = 'France';

-- 4. Joining with Aggregation (Business Intelligence)
-- Calculate total spending per Customer Name.
-- This combines Day 9 (Group By) with Day 10 (Join).
SELECT 
    c.first_name,
    c.last_name,
    SUM(p.amount) AS total_spend
FROM customer c
INNER JOIN payment p 
    ON c.customer_id = p.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_spend DESC
LIMIT 5;
```