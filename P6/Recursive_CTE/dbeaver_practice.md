`RECURSIVE CTE`

**Database: Pagila**

```sql
-- Setup: Create a tiny Org Chart
CREATE TABLE company_org (
    emp_id INT PRIMARY KEY,
    name TEXT,
    manager_id INT -- Points to emp_id
);

INSERT INTO company_org VALUES 
(1, 'Alice (CEO)', NULL),
(2, 'Bob (VP)', 1),
(3, 'Charlie (VP)', 1),
(4, 'David (Manager)', 2),
(5, 'Eve (Intern)', 4);

-- 1. The "Who reports to whom?" Query
-- We want to calculate the "Level" (Depth) of each employee.
WITH RECURSIVE hierarchy AS (
    -- ANCHOR: Start with the Boss (Level 1)
    SELECT 
        emp_id, 
        name, 
        manager_id, 
        1 as level
    FROM company_org
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- RECURSIVE: Find employees who report to the people found above
    SELECT 
        e.emp_id, 
        e.name, 
        e.manager_id, 
        h.level + 1 -- Increment level
    FROM company_org e
    JOIN hierarchy h ON e.manager_id = h.emp_id
)
SELECT * FROM hierarchy ORDER BY level;

-- 2. Generating Paths (Breadcrumbs)
-- We want a column looking like "Alice > Bob > David"
WITH RECURSIVE paths AS (
    SELECT 
        emp_id, 
        name, 
        CAST(name AS TEXT) as path
    FROM company_org
    WHERE manager_id IS NULL
    
    UNION ALL
    
    SELECT 
        e.emp_id, 
        e.name, 
        h.path || ' > ' || e.name -- Concatenate path
    FROM company_org e
    JOIN paths h ON e.manager_id = h.emp_id
)
SELECT * FROM paths;
```