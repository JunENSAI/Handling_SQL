### Question 1

**List all payments. Calculate a Running Count of payments (1, 2, 3...) ordered by payment date.**

```sql
SELECT
    amount,
    COUNT(*) OVER (ORDER BY payment_date) as running_count_payments
FROM payment;
```

### Question 2

**Calculate the Running Total Revenue (SUM(amount)) for the entire company, but ordered by payment_id. Return payment_id, amount, and running_total.**

```sql
SELECT 
    payment_id,
    amount,
    SUM(amount) OVER (ORDER BY payment_id) as running_total
FROM payment;
```

### Question 3

**We want to see the running total of rental durations for Customer 1.**

**Calculate the duration of each rental.**

**Calculate the Running Average duration (AVG) for Customer 1, ordered by rental date.**

**Include a column that shows the Total Lifetime Duration (Sum of all durations) for that customer on every row (so we can compare the running average to the total). Return: rental_date, duration, running_avg, total_lifetime_duration.**

```sql
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
```