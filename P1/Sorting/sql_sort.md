## 1. ORDER BY (Sorting)

By default, SQL does **not** guarantee any specific order. If you want data sorted, you must explicitly ask for it.

* **Syntax:** `ORDER BY column_name [ASC | DESC]`

* **ASC:** Ascending (A-Z, 0-9). Default if you don't specify.

* **DESC:** Descending (Z-A, 9-0).

* **Multi-Column Sort:** `ORDER BY last_name ASC, first_name ASC`.

    * *Logic:* It sorts everyone by Last Name first. If two people have the same Last Name, it breaks the tie using First Name.

**Order of Execution Update:**

1.  `FROM` (Get table)

2.  `WHERE` (Filter rows)

3.  `SELECT` (Pick columns)

4.  `ORDER BY` (Sort the final list)

5.  `LIMIT` (Cut it off)

---

## 2. Boolean Logic (AND, OR, NOT)

This is standard Boolean Algebra, but the **Order of Operations** (Precedence) causes many bugs.

* **Priority:** `parentheses ()` > `NOT` > `AND` > `OR`.

* **The Trap:**

    * `A AND B OR C` is interpreted as `(A AND B) OR C`.

    * If you want "A must be true, and then either B or C", you **must** write: `A AND (B OR C)`.

---

## 3. NULLs in Sorting

* In PostgreSQL, `NULL` values are considered **larger** than any non-null value.

* `ORDER BY column ASC` -> NULLs appear at the very end.

* `ORDER BY column DESC` -> NULLs appear at the very top.

* **Fix:** Use `NULLS LAST` or `NULLS FIRST` to control this explicitly.

    * e.g., `ORDER BY cost DESC NULLS LAST`.

---