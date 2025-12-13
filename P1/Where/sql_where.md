## 1. The Logic of Filtering
In the Order of Execution, `WHERE` happens **immediately after** `FROM`.

1.  **FROM**: The DB grabs the table.

2.  **WHERE**: The DB scans every row and asks: "Does this row satisfy the condition?" (True/False).

3.  **SELECT**: The DB returns only the True rows.

* **Critical Rule**: You cannot use an **Alias** defined in `SELECT` inside the `WHERE` clause.
    * *Why?* Because `WHERE` runs before `SELECT` happens. The alias doesn't exist yet!

---

## 2. Standard Operators

* **Equality**: `=` (Not `==` like in Python!)

* **Inequality**: `<>` or `!=`

* **Comparison**: `>`, `<`, `>=`, `<=`

---

## 3. The Special Operators

### A. BETWEEN (Ranges)

Instead of writing `price >= 5 AND price <= 10`, you use:

`WHERE price BETWEEN 5 AND 10`.

* *Note:* `BETWEEN` is **inclusive** (it includes 5 and 10).

### B. IN (Sets)

Instead of writing `id = 1 OR id = 2 OR id = 3`, you use:

`WHERE id IN (1, 2, 3)`.

* *Math:* $x \in S$ (x is an element of set S).

### C. LIKE & ILIKE (Pattern Matching)

* **Wildcards**:

    * `%`: Matches any sequence of characters (0 to infinity).

    * `_`: Matches exactly one character.

* **Case Sensitivity**:

    * `LIKE 'A%'`: Matches 'Apple', but NOT 'apple'.

    * `ILIKE 'A%'` (**Postgres Special**): Matches 'Apple', 'apple', 'APPLE'. (Case Insensitive).

### D. IS NULL (The Void)

In databases, `NULL` means "Unknown" or "Missing".

* $NULL = NULL$ evaluates to **Unknown** (not True).

* **Never** use `WHERE column = NULL`.

* **Always** use `WHERE column IS NULL` or `WHERE column IS NOT NULL`.

---