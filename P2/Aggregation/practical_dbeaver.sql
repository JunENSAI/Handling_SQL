-- AGGREGATION : Pagila DB

-- 1. Simple Counting
-- How many movies are in our database?
SELECT COUNT(*) AS total_movies
FROM film;

-- 2. Count vs Count(Column)
-- The 'address2' column often has empty values. 
SELECT 
	COUNT(*) AS total_rows,           -- Counts every line
	COUNT(address2) AS filled_addresses -- Counts only non-nulls
FROM address;

-- 3. Financials (SUM and AVG)
-- What is the total revenue of the company? 
-- And what is the average payment amount?
SELECT 
	SUM(amount) AS total_revenue,
	AVG(amount) AS average_payment
FROM payment;

-- 4. Statistics (MIN and MAX)
-- What is the cheapest and most expensive replacement cost for a movie?
SELECT 
	MIN(replacement_cost) AS min_cost,
	MAX(replacement_cost) AS max_cost
FROM film;

-- 5. Using Logic with Aggregates
-- You can filter rows BEFORE you aggregate them.
-- Question: What is the total revenue strictly from customers paying more than $5?
SELECT SUM(amount) AS premium_revenue
FROM payment
WHERE amount > 5.00;

-- 6. Count Distinct
-- We have many payments, but how many UNIQUE customers made those payments?
SELECT 
	COUNT(*) AS total_payments,
	COUNT(DISTINCT customer_id) AS unique_customers
FROM payment;
