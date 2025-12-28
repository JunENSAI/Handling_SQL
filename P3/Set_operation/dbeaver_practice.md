`SET OPERATIONS`

**Database: Pagila**

```sql
-- 1. UNION ALL (The Append)
-- We want a list of all names in our database (Actors AND Customers).
SELECT first_name, last_name FROM actor
UNION ALL
SELECT first_name, last_name FROM customer;

-- 2. UNION (The Distinct List)
-- Are there any names that are shared?
-- If "Jennifer Davis" is an actor AND a customer, UNION will show her once. UNION ALL shows her twice.
SELECT first_name, last_name FROM actor
UNION
SELECT first_name, last_name FROM customer;

-- 3. INTERSECT (Finding Overlaps)
-- Who is both an Actor and a Customer? (Based on name)
SELECT first_name, last_name FROM actor
INTERSECT
SELECT first_name, last_name FROM customer;

-- 4. EXCEPT (The Difference)
-- Find films that are in the Film table, but NOT in the Inventory table.
SELECT film_id FROM film
EXCEPT
SELECT film_id FROM inventory;
```