### Question 1

**List all first_names from the staff table and all first_names from the customer table combined into one list.**

```sql
SELECT first_name FROM staff
UNION ALL
SELECT first_name FROM customer;
```

### Question 2

**Find the customer_ids of people who have rented a movie but have never made a payment.**

```sql
SELECT customer_id FROM rental
EXCEPT
SELECT customer_id FROM payment;
```

### Question 3

**Find first_names that are shared between actor and customer tables. Return the first_name. However, you must filter the actors to only those whose last name starts with 'D' and customers whose last name starts with 'D'.**


```sql
SELECT first_name FROM actor
WHERE first_name LIKE 'D%'
INTERSECT
SELECT first_name FROM customer
WHERE first_name LIKE 'D%';
```