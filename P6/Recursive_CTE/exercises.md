## Question 1

Write a Recursive CTE that generates the numbers 1, 2, 4, 8, 16 ... up to 1024 (Powers of 2). Stop when val < 1024.

```sql
WITH RECURSIVE power_number_two AS (
    SELECT 1 as val
    
    UNION ALL

    SELECT val * 2
    FROM power_number_two
    WHERE val < 1024
)
SELECT * FROM power_number_two;
```


## Question 2

Using the company_org table from the lab: Write a Recursive CTE that finds all descendents of 'Bob (VP)'.

- Start the Anchor at Bob

- Find everyone below him.

```sql
WITH RECURSIVE hierarchy AS (
    SELECT emp_id, name, manager_id, 0 as level
    FROM company_org
    WHERE name LIKE 'Bob%'
    
    UNION ALL
    
    SELECT e.emp_id, e.name, e.manager_id, h.level + 1
    FROM company_org e
    JOIN hierarchy h ON e.manager_id = h.emp_id
    )
SELECT name, level FROM hierarchy ORDER BY level, manager_id;
```

## Question 3

Calculated factorials (5! = 5 * 4 * 3 * 2 * 1 = 120). Write a Recursive CTE that columns: step, factorial_value. It should generate: 1, 1 2, 2 3, 6 4, 24 5, 120 Hint: You need two columns in your recursive query: the current counter (1, 2, 3) and the cumulative math result.

```sql
WITH FactorialCTE AS (
    SELECT 1 AS x, 1 AS y
    UNION ALL
    SELECT x + 1, y * (x + 1)
    FROM FactorialCTE
    WHERE x < 5
)
SELECT * FROM FactorialCTE;
```