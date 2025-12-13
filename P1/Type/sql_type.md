## 1. The Core Data Types

Postgres is strict. Here are the types you will use 90% of the time:

### A. Numbers

* **INTEGER (INT):** Whole numbers (e.g., `1`, `42`, `-5`). No decimals.

    * *Trap:* `5 / 2` in Integer math equals `2`, not `2.5`.

* **NUMERIC / DECIMAL:** Exact decimals. Use this for **Money**.

    * *Why?* Floats have rounding errors. `NUMERIC` is precise.

* **FLOAT / REAL:** Approximate decimals (Scientific data).

### B. Strings (Text)

* **VARCHAR(n):** Variable-length text with a limit of *n* characters.

* **TEXT:** Unlimited length text. (In Postgres, `TEXT` is actually preferred over `VARCHAR` for performance reasons unless you strictly need a limit).

* **CHAR(n):** Fixed length. If you store "Hi" in `CHAR(5)`, it saves "Hi   " (padded with spaces). Avoid this.

### C. Boolean

* **BOOLEAN:** `TRUE`, `FALSE`, or `NULL`.

---

## 2. Casting (Converting Types)

Sometimes you have a number stored as text (e.g., `'100'`) and you need to do math on it. You must **Cast** it.

### Syntax

1.  **Standard SQL:** `CAST(column_name AS new_type)`

2.  **Postgres Shorthand:** `column_name::new_type` (Use this one, it's faster to write).

---

## 3. The "Integer Division" Trap
If you divide two integers, SQL assumes the result should be an integer.

* `SELECT 10 / 4;` -> Result: `2`

* `SELECT 10::float / 4;` -> Result: `2.5` (Because we cast the numerator to a float first).

---