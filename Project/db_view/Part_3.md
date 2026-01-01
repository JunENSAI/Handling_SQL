## The "Master View"

Business users hate joining 4 tables. They just want to see "Portfolio Performance". 

**Task:** Create a View named `v_portfolio_performance` that combines all our work.

Columns required:

- `user_name`

- `company_name`

- `quantity`

- `purchase_price` (What they bought it for)

- `current_price` (Use the logic from Question 3 above to get the latest price)

- `gain_loss` (Current Value - Original Cost)

## Dashboard

Now we visualize. We will query our database and plot the stock price history using matplotlib (standard plotting library).