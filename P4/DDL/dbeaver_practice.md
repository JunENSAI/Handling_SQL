`CREATE & ALTER`

**Database: Pagila**

```sql
-- 1. Create a Table
CREATE TABLE my_staff_log (
    log_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    action VARCHAR(20),
    log_time TIMESTAMP DEFAULT NOW()
);

-- 2. Check if it exists
SELECT * FROM my_staff_log;

-- 3. Testing the Defaults (Mini-DML Preview)
INSERT INTO my_staff_log (username, action) 
VALUES ('Mike', 'Login');

SELECT * FROM my_staff_log;

-- 4. Altering the Table
ALTER TABLE my_staff_log 
ADD COLUMN ip_address VARCHAR(15);

-- 5. Dropping
DROP TABLE my_staff_log;
