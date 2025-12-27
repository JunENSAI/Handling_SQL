### Question 1

**Write a query using payment table. List payment_id, amount, and the amount of the next payment ordered by payment_id.**

```sql
SELECT
    payment_id,
    amount,
    LEAD(amount, 1) OVER (ORDER BY payment_id) as next_payment
FROM payment
```

### Question 2

**Calculate the difference between the current payment amount and the previous payment amount for Customer 1 using LAG. Return payment_date, amount, previous_amount, and difference.**


```sql
SELECT
    payment_date,
    amount,
    LAG(amount, 1) OVER (PARTITION BY customer_id ORDER BY payment_date) as previous_amount,
    amount - LAG(amount, 1) OVER (PARTITION BY customer_id ORDER BY payment_date) as difference
FROM payment
WHERE customer_id = 1;
```


### Question 3

**Find the duration of each rental (return date - rental date). Then, using LAG, compare the current rental's duration to the previous rental's duration for each customer. Return: customer_id, rental_id, current_duration, previous_duration, and growth_duration**

```sql
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
```