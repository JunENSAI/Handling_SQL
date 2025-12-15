/* STRING MANIPULATION --
   Database: Pagila
*/

```sql
-- 1. Concatenation (The || Operator)
-- Create a "Full Name" column.
SELECT 
	first_name, 
	last_name,
	first_name || ' ' || last_name AS full_name
FROM customer
LIMIT 5;

-- 2. Formatting (INITCAP)
-- Emails are often stored in lower case, names in upper. Let's make it look nice.
SELECT 
	email,
	LOWER(email) AS clean_email,
	INITCAP(first_name) AS pretty_name
FROM customer
LIMIT 5;

-- 3. Extracting Data (LEFT/RIGHT)
-- Let's just get the first initial of the last name.
SELECT 
	first_name,
	last_name,
	first_name || ' ' || LEFT(last_name, 1) || '.' AS short_name
FROM customer
LIMIT 5;

-- 4. Finding patterns (Length)
-- Find customers with unusually short first names (less than 3 chars).
SELECT first_name, LENGTH(first_name)
FROM customer
WHERE LENGTH(first_name) < 3;

-- 5. Parsing (The Hard Stuff)
-- Challenge: Extract only the domain from the email address (e.g., 'gmail.com').
-- Logic: Find the '@', take everything after it.
SELECT 
	email,
	POSITION('@' IN email) AS at_symbol_loc,
	SUBSTRING(email FROM POSITION('@' IN email) + 1) AS domain_only
FROM customer
LIMIT 10;
```