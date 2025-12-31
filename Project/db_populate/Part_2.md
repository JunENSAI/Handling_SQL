# The Population (Python Automation)

## The Goal

- We need to insert data into our new schema.

- Manually writing `INSERT INTO` for 100 days of stock prices is impossible. 

- We will use Python.

## The Strategy

1.  **Libraries:** `yfinance` (Yahoo Finance) is a free Python library to get real stock data. `pandas` will handle the cleaning.

2.  **The Loop:**

    * List of Tickers: `['AAPL', 'MSFT', 'GOOGL']`.

    * For each ticker:

        1.  Insert into `companies` table.

        2.  Download 1 month of history.

        3.  Insert into `stock_prices` table.

---

## New Concept: Bulk Inserts

Inserting 1 row at a time is slow.

Pandas `to_sql` uses a method called `executemany` which is faster, but for millions of rows, we often use the `COPY` command (advanced). For this project, `to_sql` is perfect.

## Queries SQL

- Write a SQL query that joins stock_prices and companies. Select: company_name, price_date, close_price. Filter: Show only 'Apple Inc.' prices.

- Write a SQL query to calculate the Daily Volatility for every row.

    - Formula: close_price - open_price.

    - Select: company_id, price_date, and volatility.

    - Order by: volatility DESC (Who had the biggest jump?).

- Write a query to calculate the Total Current Value of 'Alice's' portfolio.

    - Assume the "Current Price" is simply the close_price from the most recent date in the stock_prices table.

    - Hint: This requires joining holdings -> companies -> stock_prices. You might need a CTE to find the "latest price" for each company first.

---