-- LAG & LEAD : Pagila DB

-- 1. Simple LAG
-- Show the payment amount, and the amount of the PREVIOUS payment, side-by-side.
SELECT 
    payment_id,
    customer_id,
    amount,
    payment_date,
    LAG(amount, 1) OVER (ORDER BY payment_date) as prev_payment
FROM payment
LIMIT 15;

-- 2. Calculating Difference (The Delta)
-- How much more (or less) did this customer pay compared to their last visit?
SELECT 
    customer_id,
    payment_date,
    amount,
    LAG(amount, 1) OVER (PARTITION BY customer_id ORDER BY payment_date) as last_amount,
    amount - LAG(amount, 1) OVER (PARTITION BY customer_id ORDER BY payment_date) as difference
FROM payment
ORDER BY customer_id, payment_date
LIMIT 20;

-- 3. LEAD (Looking into the future)
-- What is the NEXT film this customer rented?
SELECT 
    customer_id,
    rental_date,
    rental_id,
    LEAD(rental_date, 1) OVER (PARTITION BY customer_id ORDER BY rental_date) as next_rental_date
FROM rental
ORDER BY customer_id, rental_date
LIMIT 20;

-- 4. Days Between Rentals (Churn Analysis)
-- Calculate how many days passed between a customer's rentals.
SELECT 
    customer_id,
    rental_date,
    LEAD(rental_date, 1) OVER (PARTITION BY customer_id ORDER BY rental_date) as next_date,
    LEAD(rental_date, 1) OVER (PARTITION BY customer_id ORDER BY rental_date) - rental_date as time_gap
FROM rental
LIMIT 20;
