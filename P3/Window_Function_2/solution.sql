-- Question 1

SELECT
    payment_id,
    amount,
    LEAD(amount, 1) OVER (ORDER BY payment_id) as next_payment
FROM payment;

-- Question 2

SELECT
    payment_date,
    amount,
    LAG(amount, 1) OVER (PARTITION BY customer_id ORDER BY payment_date) as previous_amount,
    amount - LAG(amount, 1) OVER (PARTITION BY customer_id ORDER BY payment_date) as difference
FROM payment
WHERE customer_id = 1;

-- Question 3

WITH rental_durations AS (
    SELECT 
        customer_id,
        rental_id,
        rental_date,
        return_date - rental_date AS current_duration
    FROM rental
)
SELECT 
    customer_id,
    rental_id,
    current_duration,
    LAG(current_duration, 1) OVER (PARTITION BY customer_id ORDER BY rental_date) AS previous_duration,
    current_duration - 
    LAG(current_duration, 1) OVER (PARTITION BY customer_id ORDER BY rental_date) AS growth_duration
FROM rental_durations;