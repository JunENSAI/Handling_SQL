## 1. The Concept

Standard SQL looks at one row at a time. `LAG` and `LEAD` allow a row to "look around" at its neighbors.

* **LAG(column, n):** Look *backwards* `n` rows.

* **LEAD(column, n):** Look *forwards* `n` rows.

---

## 2. The Use Case: Growth & Difference

This is how you calculate **Month-over-Month (MoM)** or **Year-over-Year (YoY)** growth in pure SQL.

Formula: `(Current_Value - Previous_Value) / Previous_Value`

To do this, you need the "Previous Value" to exist on the "Current Row". `LAG` does exactly that.

---

## 3. Syntax
```sql
SELECT 
    month,
    revenue,
    LAG(revenue, 1) OVER (ORDER BY month) as previous_month_revenue
FROM monthly_sales;
```

*Note*: The first row has no "previous" row, so LAG returns NULL. You can specify a default value if you want: `LAG(column, 1, 0)` makes the first row return 0 instead of NULL.

---