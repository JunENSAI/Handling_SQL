## 1. The Concept
You already know `SUM()`.

* `SUM(amount)` collapses all rows into one total.

* `SUM(amount) OVER (PARTITION BY customer)` calculates the total for that customer on every row (the value repeats).

* **`SUM(amount) OVER (ORDER BY date)`** calculates a **Running Total**.

---

## 2. Running Total (Cumulative Sum)

By adding `ORDER BY` inside the `OVER()` clause of an aggregate, you tell SQL:
"Sum up everything from the start **up to the current row**."

---

## 3. Moving Average
You can define a "Frame" to only look at recent rows (e.g., the last 3 days).

* Syntax: `AVG(amount) OVER (ORDER BY date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)`

* This calculates the average of Today + Yesterday + Day Before Yesterday.

---

## 4. Visualizing the Frame

* **UNBOUNDED PRECEDING:** From the very beginning.

* **CURRENT ROW:** Stop here.

* **1 PRECEDING:** Just the one row before.

---