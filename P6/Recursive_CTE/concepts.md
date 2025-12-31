## 1. The Concept

- Normal SQL is set-based (grab these rows).

- `Recursive SQL is iterative `(grab row A, then find who reports to A, then find who reports to them...). `It loops until it runs out of data.`

---

## 2. The Syntax Structure

A Recursive CTE has three parts:

1.  **The Anchor Member:** The starting point (e.g., The CEO, or the number 1).

2.  **UNION ALL:** The glue.

3.  **The Recursive Member:** The query that references the CTE itself to find the "next" level.

```sql
WITH RECURSIVE count_to_ten AS (
    -- 1. Anchor (Start)
    SELECT 1 as val
    
    UNION ALL
    
    -- 3. Recursive (Loop)
    SELECT val + 1 
    FROM count_to_ten 
    WHERE val < 10 -- Stop condition
)
SELECT * FROM count_to_ten;
```

## 3. Use Case: Hierarchies (Adjacency List)

Imagine an employees table where ``manager_id`` points to another row in the same table.

- `Anchor:` Find the CEO (Manager is NULL).

- `Recursion:` Find everyone whose manager_id equals the employee_id found in the previous step.

---