-- DML : Pagila DB

-- Setup: Create a sandbox table
CREATE TABLE my_todo (
    task_id SERIAL PRIMARY KEY,
    task TEXT,
    status TEXT DEFAULT 'pending'
);

-- 1. Basic Insert
INSERT INTO my_todo (task) VALUES ('Buy Milk');

-- 2. Insert Returning 
INSERT INTO my_todo (task) 
VALUES ('Learn SQL') 
RETURNING task_id, task, status;

-- 3. Bulk Insert
INSERT INTO my_todo (task) 
VALUES 
    ('Walk the dog'),
    ('Call Mom'),
    ('Do Laundry');

-- 4. Update
UPDATE my_todo 
SET status = 'done' 
WHERE task_id = 1;

-- 5. Delete
DELETE FROM my_todo 
WHERE task LIKE '%Laundry%';

-- Check results
SELECT * FROM my_todo;

-- 6. Upsert (On Conflict)

INSERT INTO my_todo (task_id, task) VALUES (1, 'Buy Soy Milk')
ON CONFLICT (task_id) 
DO UPDATE SET task = EXCLUDED.task; -- "EXCLUDED" means the value we tried to insert

SELECT * FROM my_todo WHERE task_id = 1;
