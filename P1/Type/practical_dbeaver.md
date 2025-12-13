/* LAB: DATA TYPES & CASTING
   Database: Pagila
*/

```sql

-- 1. Checking Data Types
-- In DBeaver, you can see types in the "Properties" tab of a table.
-- Or, verify a specific value's type using pg_typeof()
SELECT 
	'100' AS string_val,
	pg_typeof('100') AS type_1,
	100 AS int_val,
	pg_typeof(100) AS type_2;

-- NOW, let's look at a pure integer example:
SELECT 
	10 / 4 AS integer_math,          -- Result: 2
	10.0 / 4 AS implicit_float,      -- Result: 2.500...
	10::float / 4 AS explicit_cast;  -- Result: 2.5

-- 2. Converting Text to Numbers
-- Imagine we imported data and the prices were saved as text strings like '$2.99'.
-- We try to cast it.
SELECT 
	'$2.99' AS raw_text,
	-- '$2.99'::numeric  <-- THIS WILL FAIL (Error: invalid input syntax for type numeric)
	
	-- Fix: We must clean the string first (remove $) then cast.
	TRIM(LEADING '$' FROM '$2.99')::numeric AS cleaned_number;

-- 4. Boolean Logic
-- Postgres booleans are smart.
SELECT 
	true, 
	'yes'::boolean, 
	'on'::boolean, 
	1::boolean; -- All of these evaluate to TRUE
```