## 1. The Concept

Aggregate functions take **many rows** and collapse them into **one value**.

* *Math:* $f(x_1, x_2, ..., x_n) = y$

* *Example:* Input 1000 prices -> Output 1 average price.

---

## 2. The Big Five Functions

1.  **COUNT()**: Counts items.

    * `COUNT(*)`: Counts **rows** (including NULLs). "How many lines are in the table?"

    * `COUNT(column)`: Counts **non-null values** in that column. "How many customers have an email address?"

2.  **SUM()**: Adds up numeric values. (Returns NULL if no rows found).

3.  **AVG()**: Calculates the mean.

    * *Note:* It ignores NULLs in the calculation.

4.  **MIN()**: Finds the lowest value (works on Numbers, Dates, and Text).

5.  **MAX()**: Finds the highest value.

---

## 3. The "Distinct" Twist

You can combine these.

* `COUNT(DISTINCT customer_id)`: "How many *unique* customers bought something today?" (Ignores repeat visits).

---

## 4. The Golden Rule of Aggregation

**You cannot mix normal columns with aggregate functions** (unless you use `GROUP BY`, which is tomorrow's topic).

* *Wrong:* `SELECT title, AVG(length) FROM film;`

    * *Why:* `title` returns 1000 rows. `AVG(length)` returns 1 row. The database doesn't know how to align them.

* *Right:* `SELECT AVG(length) FROM film;` (Returns just the average).

---