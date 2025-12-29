`TRANSACTIONS`

**Database: Pagila**
```sql
-- Setup: Create a simple bank table
CREATE TABLE my_bank (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    balance INT
);

INSERT INTO my_bank (name, balance) VALUES ('Alice', 1000), ('Bob', 500);

-- 1. The Happy Path (Commit)
BEGIN;
    -- Move $100 from Alice to Bob
    UPDATE my_bank SET balance = balance - 100 WHERE name = 'Alice';
    UPDATE my_bank SET balance = balance + 100 WHERE name = 'Bob';
COMMIT; -- Changes are saved now.

SELECT * FROM my_bank; 

-- 2. The Error Path (Rollback)
BEGIN;
    -- Move $200 from Alice...
    UPDATE my_bank SET balance = balance - 200 WHERE name = 'Alice';
    
    -- OOPS! Power failure / Error
    -- We decide NOT to give it to Bob.
    -- If we stopped here without a transaction, Alice would be out $200.
    
    ROLLBACK; -- Undo everything in this block.

SELECT * FROM my_bank;
-- Alice: 900. (The -200 never happened).

-- 3. Savepoints (Advanced)
BEGIN;
    UPDATE my_bank SET balance = balance - 10 WHERE name = 'Alice';
    SAVEPOINT step_1;
    
    UPDATE my_bank SET balance = balance - 5000 WHERE name = 'Alice'; -- This will fail later
    
    ROLLBACK TO SAVEPOINT step_1; -- We undo the 5000, but keep the 10.
COMMIT;
```