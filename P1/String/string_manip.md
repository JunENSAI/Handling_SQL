## 1. Concatenation (Gluing strings)

* **Standard SQL:** `CONCAT(str1, str2)`

* **Postgres Shorthand:** `str1 || str2` (The double pipe operator).

* *Tip:* If you concatenate `String + NULL`, the result is usually `NULL` (unless you use `CONCAT` which handles nulls gracefully).

---

## 2. Slicing and Dicing

* **LENGTH(str):** Returns the number of characters.

* **SUBSTRING(str FROM start FOR length):** Extracts part of the string.

    * **CRITICAL DIFFERENCE:** SQL is **1-indexed**. The first character is at position 1. Python is 0-indexed.

    * `SUBSTRING('Hello', 1, 2)` -> 'He' (SQL)

    * `string[0:2]` -> 'He' (Python)
    
* **POSITION(substring IN string):** Finds the index where a substring starts.

---

## 3. Cleaning

* **TRIM(str):** Removes leading and trailing spaces.

* **UPPER(str) / LOWER(str):** Changes case.

* **INITCAP(str):** Capitalizes the first letter of each word (Title Case).

* **REPLACE(str, old, new):** Swaps text.

---

## 4. Advanced (Pattern Matching)

* **LEFT(str, n) / RIGHT(str, n):** Quick way to get the start/end of a string.

---