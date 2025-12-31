# Part 1 - The Design

## The Scenario
You are building a **Stock Market Analysis Tool**.
We need to track **Companies**, their **Daily Stock Prices**, and our user's **Portfolios** (what stocks they own and when they bought them).

## The Goal
Design a Normalized (3NF) Schema to handle this data.

## Requirements
1.  **Table: `companies`**
    * `company_id` (PK, Ticker Symbol like 'AAPL', 'TSLA')
    * `company_name`
    * `sector` (Tech, Health, etc.)
2.  **Table: `stock_prices`**
    * Links to a Company.
    * Records the `price_date`, `open_price`, `close_price`, and `volume`.
    * *Constraint:* Price cannot be negative.
    * *Composite PK:* A company can only have one price entry per date.
3.  **Table: `portfolios`**
    * `portfolio_id` (PK, Serial)
    * `user_name`
    * `created_at`
4.  **Table: `holdings`** (The Link Table)
    * Links a Portfolio to a Company.
    * `quantity` (How many shares owned).
    * `purchase_price` (Cost basis).
    * `purchase_date`.

## Your Task
Write the `CREATE TABLE` statements for these 4 tables.
Pay attention to:
* **Foreign Keys** (Linking tables correctly).
* **Data Types** (Use `DECIMAL` for money, not FLOAT).
* **Constraints** (No negative prices).