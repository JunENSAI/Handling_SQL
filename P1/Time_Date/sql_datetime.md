## 1. The Data Types

* **DATE:** Just the calendar date (YYYY-MM-DD). No time.

* **TIMESTAMP:** Date + Time (YYYY-MM-DD HH:MM:SS).

* **TIMESTAMPTZ:** Timestamp **with Time Zone**.

    * *Best Practice:* Always use `TIMESTAMPTZ` if your app spans multiple countries. Postgres stores it in UTC but displays it in your local time.

---

## 2. Getting "Now"

* `CURRENT_DATE`: Returns today's date (e.g., `2025-12-13`).

* `NOW()`: Returns the current timestamp with microsecond precision.

---

## 3. Date Arithmetic

You can do math with dates just like numbers.

* **Intervals:** You can add specific units of time.

    * `NOW() + INTERVAL '10 days'`

    * `NOW() - INTERVAL '3 months'`

* **Difference:** Subtracting two dates gives you an **Interval** (duration) or an integer (days), depending on the types.

    * `return_date - rental_date` = How long they kept the DVD.

---

## 4. Extracting Parts

Sometimes you only want the "Year" or the "Day of the Week" for a report.

* **Syntax:** `EXTRACT(field FROM source)`

* **Examples:**

    * `EXTRACT(YEAR FROM rental_date)`

    * `EXTRACT(DOW FROM rental_date)` -> Day of Week (0=Sunday, 6=Saturday).

* **Truncating:** `DATE_TRUNC('month', rental_date)` rounds the date down to the first of the month. Perfect for monthly grouping.

---