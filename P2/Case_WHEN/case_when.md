## 1. The Concept

Data in databases is often raw numbers (Length = 95 minutes). Business users want categories ("Short", "Medium", "Long").
`CASE WHEN` lets you translate raw data into business logic inside your query.

---

## 2. Syntax
It looks verbose, but the structure is simple:
```sql
CASE
    WHEN condition_1 THEN result_1
    WHEN condition_2 THEN result_2
    ELSE result_3
END
```
---

## 3. Two Ways to Write It

### A. The General Form (Most Common)

Flexible conditions.

```SQL

CASE 
    WHEN rating = 'G' THEN 'Kids'
    WHEN length > 120 THEN 'Long Movie'
    ELSE 'Standard'
END
```

### B. The Simple Form (Switch)

Checking one specific column for exact matches.

```SQL

CASE rating
    WHEN 'G' THEN 'Kids'
    WHEN 'R' THEN 'Adults'
    ELSE 'Others'
END
```
---
