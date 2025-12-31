## Question 1

Write a PL/pgSQL function named `get_customer_email(cust_id INT)` that returns TEXT.

```sql
CREATE OR REPLACE FUNCTION get_customer_email(cust_id INT)
RETURNS TEXT AS $$
DECLARE
    found_email TEXT;
BEGIN
    SELECT email INTO found_email 
    FROM customer 
    WHERE customer_id = cust_id;
    
    RETURN found_email;
END;
$$ LANGUAGE plpgsql;
```

## Question 2
Write a function is_premium_customer(cust_id INT) that returns BOOLEAN.

- Logic: Sum the total payments for this customer.

- IF total > 100, Return TRUE.

- ELSE Return FALSE.

```sql
CREATE OR REPLACE FUNCTION is_premium_customer(cust_id INT)
RETURNS BOOLEAN AS $$
DECLARE
    total_spend NUMERIC;
BEGIN
    SELECT SUM(amount) INTO total_spend 
    FROM payment 
    WHERE customer_id = cust_id;

    IF total_spend IS NULL THEN 
        total_spend := 0; 
    END IF;

    IF total_spend > 100 THEN
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END IF;
END;
$$ LANGUAGE plpgsql;
```

## Question 3

Write a Procedure (Not a function) named `give_bonus_to_staff(staff_id_input INT, bonus_amount NUMERIC)`.

**Task**: Let's pretend we have a staff_audit table. Insert a row into it.

- Step 1: CREATE TABLE staff_audit (staff_id INT, message TEXT, amount NUMERIC);

- Step 2: The Procedure inserts: (staff_id_input, 'Bonus Given', bonus_amount).

- Step 3: Call it using CALL give_bonus_to_staff(1, 500);.

```sql
CREATE TABLE staff_audit (
    audit_id SERIAL PRIMARY KEY,
    staff_id INT,
    message TEXT,
    amount NUMERIC
);

CREATE OR REPLACE PROCEDURE give_bonus_to_staff(
   staff_id_input INT,
   bonus_amount NUMERIC
)
AS $$
BEGIN
    INSERT INTO staff_audit (staff_id, message, amount) 
    VALUES (staff_id_input, 'Bonus Given', bonus_amount);
END;
$$ LANGUAGE plpgsql;

CALL give_bonus_to_staff(1, 500);;
```


