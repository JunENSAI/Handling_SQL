-- Question 1

SELECT first_name FROM staff
UNION ALL
SELECT first_name FROM customer;

-- Question 2

SELECT customer_id FROM rental
EXCEPT
SELECT customer_id FROM payment;

-- Question 3

SELECT first_name FROM actor
WHERE first_name LIKE 'D%'
INTERSECT
SELECT first_name FROM customer
WHERE first_name LIKE 'D%';