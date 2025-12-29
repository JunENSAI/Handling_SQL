## Question 1

**Write the SQL to create a standard View named rich_customers that selects first_name, last_name, and email from the customer table, but only for inactive customers (active = 0).**

```sql
CREATE VIEW rich_customers AS
SELECT 
    first_name,
    last_name
    email
FROM customer
WHERE active = 0;
```


## Question 2

**Write the SQL to create a Materialized View named daily_sales_cache that calculates the total amount from the payment table grouped by payment_date (casted to Date).**

```sql
CREATE MATERIALIZED VIEW daily_sales_cache AS
SELECT
    payment_date,
    SUM(amount) AS total_payment
FROM payment
GROUP BY DATE(payment_date); -- because payment_date is TIMESTAMP so every second must be counted if we don't specify DATE()
```

## Question 3

Assume that `rich_customers` view exists.

- Write a query to update the email of a user through the view.

- Can you update a View?

   - Try: UPDATE rich_customers SET email = 'new@test.com' WHERE first_name = '...';

    - If it works, explain why. If not, explain why.

```sql
UPDATE rich_customers
SET email = 'new@test.com'
WHERE first_name = 'HARRY';
```

*Note* : 

- In `PostgreSQL`, simple views (those that map 1-to-1 with a single table and don't involve Aggregates, Group By, or Distinct) are **Updatable Views**. 

- If the view had a `SUM()` or a `JOIN`, the update would fail because Postgres wouldn't know which specific row in the original table to change.