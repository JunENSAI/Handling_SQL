-- Question 1

SELECT
    amount,
    COUNT(*) OVER (ORDER BY payment_date) as running_count_payments
FROM payment;

-- Question 2

SELECT 
    payment_id,
    amount,
    SUM(amount) OVER (ORDER BY payment_id) as running_total
FROM payment;

-- Question 3

WITH rental_calc AS (
    SELECT
        customer_id,
        rental_date,
        return_date - rental_date AS duration
    FROM rental
    WHERE customer_id = 1
)
SELECT
    duration,
    rental_date,
    AVG(duration) OVER (ORDER BY rental_date) as running_avg_duration,
    SUM(duration) OVER () as total_lifetime_duration
FROM rental_calc;