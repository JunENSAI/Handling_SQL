`RUNNING TOTALS`

**Database: Pagila**

```sql
-- 1. Cumulative Revenue
-- How much money have we made over time?
-- We order by payment_date, so the sum grows row by row.
SELECT 
    payment_date,
    amount,
    SUM(amount) OVER (ORDER BY payment_date) as running_total_revenue
FROM payment
LIMIT 20;

-- 2. Running Total Per Customer
-- How much has EACH customer spent over their lifetime?
-- When the customer_id changes, the sum resets to 0.
SELECT 
    customer_id,
    payment_date,
    amount,
    SUM(amount) OVER (PARTITION BY customer_id ORDER BY payment_date) as customer_running_spend
FROM payment
ORDER BY customer_id, payment_date
LIMIT 20;

-- 3. Moving Average (Smoothing Data)
-- Calculate a "3-Payment Moving Average" for each customer.
-- This helps smooth out spikes (e.g., one huge payment followed by small ones).
SELECT 
    customer_id,
    payment_date,
    amount,
    AVG(amount) OVER (
        PARTITION BY customer_id 
        ORDER BY payment_date 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) as moving_avg_3_payments
FROM payment
LIMIT 20;

-- 4. Percent of Total
-- How much does this specific payment contribute to the customer's TOTAL lifetime spend?
-- Denominator: SUM(amount) OVER (PARTITION BY customer_id) -> No ORDER BY means "Total for partition".
SELECT 
    customer_id,
    amount,
    SUM(amount) OVER (PARTITION BY customer_id) as total_lifetime_spend,
    amount / SUM(amount) OVER (PARTITION BY customer_id) as percent_of_total
FROM payment
ORDER BY customer_id, amount DESC
LIMIT 20;
```