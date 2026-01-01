-- Question 1

CREATE VIEW rich_customers AS
SELECT 
    first_name,
    last_name
    email
FROM customer
WHERE active = 0;

-- Question 2

CREATE MATERIALIZED VIEW daily_sales_cache AS
SELECT
    payment_date,
    SUM(amount) AS total_payment
FROM payment
GROUP BY DATE(payment_date); -- because payment_date is TIMESTAMP so every second must be counted if we don't specify DATE()

-- Question 3

UPDATE rich_customers
SET email = 'new@test.com'
WHERE first_name = 'HARRY';