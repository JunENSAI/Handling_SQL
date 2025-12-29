## Question 1 : Staff Running Total

**The Ask:** We want to see how each staff member performs month-by-month. Calculate the Total Revenue processed by each staff member for each month. Then, add a column showing the Running Total Revenue for that staff member over time (growing month by month).

**Columns:** `staff_id`, `month (truncated date)`, `monthly_revenue, running_total`.

## Question 2 : The Month-over-Month Growth 

**The Ask:** How is our total revenue growing ?

- Calculate total revenue per month.Create a column showing the Revenue of the Previous Month (side-by-side).

- Calculate the Percentage Growth from the previous month to the current month.

- Formula: $\frac{Current - Previous}{Previous} \times 100$

**Columns**: `payment_month,` `current_rev`, `prev_rev`, `growth_percent`.

## Question 3 : The Top 5 Customers

**The Ask:** Identify our top spenders. Find the Top 5 Customers by Total Spend.

**Crucial:** If two customers have spent the exact same amount, they must share the rank (e.g., both are Rank 1). The next person should be Rank 2 (Dense Rank).

**Columns:** `customer_id`, `total_spend`, `rank`.

## Question 4 : Rental Duration vs Average

**The Ask:** We want to flag rentals that were kept unusually long. List every rental. Include the customer_id, rental_id, and duration (return date - rental date). Add a column showing the Average Duration for that specific Customer. Add a column showing the Difference (This Rental's Duration - Customer's Average Duration).

**Columns:** `rental_id`, `customer_id`, `duration`, `avg_customer_duration`, `difference`.

## Question 5 :The "Binge Watcher" Metric

**The Ask:** Find customers who rented a movie less than 24 hours after their previous rental.

- For each rental, calculate the time difference from the previous rental by that same customer.

- Filter to show only rows where this difference is less than 24 hours (or INTERVAL '1 day').

**Columns:** `customer_id`, `rental_date`, `previous_rental_date`, `time_gap`.


