-- Question 1

WITH staff_monthly_sales AS (
    SELECT 
        staff_id,
        DATE_TRUNC('month', payment_date) as pay_month,
        SUM(amount) as monthly_revenue
    FROM payment
    GROUP BY staff_id, DATE_TRUNC('month', payment_date)
)
SELECT 
    staff_id,
    pay_month,
    monthly_revenue,
    SUM(monthly_revenue) OVER (
        PARTITION BY staff_id 
        ORDER BY pay_month
    ) as running_total_revenue
FROM staff_monthly_sales
ORDER BY staff_id, pay_month;


-- Note : When you didn't GROUP BY staff and month. Your result has thousands of rows (every individual payment) instead of just one row per staff/month.

-- Question 2

WITH monthly_stats AS (
    SELECT 
        DATE_TRUNC('month', payment_date) as payment_month,
        SUM(amount) as current_rev
    FROM payment
    GROUP BY DATE_TRUNC('month', payment_date)
)
SELECT 
    payment_month,
    current_rev,
    LAG(current_rev, 1) OVER (ORDER BY payment_month) as prev_rev,
    (current_rev - LAG(current_rev, 1) OVER (ORDER BY payment_month)) 
    / NULLIF(LAG(current_rev, 1) OVER (ORDER BY payment_month), 0) * 100 as growth_percent
FROM monthly_stats;

-- Question 3

WITH customer_totals AS (
    SELECT 
        customer_id,
        SUM(amount) as total_spend
    FROM payment
    GROUP BY customer_id
),
ranked_customers AS (
    SELECT 
        customer_id,
        total_spend,
        DENSE_RANK() OVER (ORDER BY total_spend DESC) as rank
    FROM customer_totals
)
SELECT * FROM ranked_customers
WHERE rank_val <= 5;

-- Note : SUM(amount) OVER (PARTITION BY customer_id) puts the total on every single row for that customer.

-- Question 4

WITH rental_duration AS (
    SELECT 
        customer_id,
        rental_id,
        return_date - rental_date as duration
    FROM rental
)
SELECT
    customer_id,
    rental_id,
    duration,
    AVG(duration) OVER(PARTITION BY customer_id) as avg_customer_duration,
    duration - AVG(duration) OVER(PARTITION BY customer_id) as difference
FROM rental_duration;

-- Question 5

WITH rental_watcher AS (
    SELECT 
        customer_id,
        rental_date,
        LAG(rental_date,1) OVER(PARTITION BY customer_id ORDER BY rental_date) as previous_rental_date,
        rental_date - LAG(rental_date,1) OVER(PARTITION BY customer_id ORDER BY rental_date) as time_gap
    FROM rental
)
SELECT
    customer_id,
    rental_date,
    previous_rental_date,
    time_gap
FROM rental_watcher
WHERE time_gap < '1day';

-- Note_correction : Without `ORDER BY` inside the OVER(), **the database doesn't know which rental came "before" the current one. It might pick a random one.
