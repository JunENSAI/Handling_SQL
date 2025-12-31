SELECT
    com.company_name,
    stpr.price_date,
    stpr.close_price
FROM companies AS com
JOIN stock_prices stpr ON
    com.company_id = stpr.company_id
WHERE com.company_name = 'Apple Inc';


-- Retrieve the volatility of company in stock_prices
SELECT
    company_id,
    price_date,
    close_price - open_price as volatility
FROM stock_prices
ORDER BY volatility DESC;

---

WITH latest_prices AS (
    SELECT DISTINCT ON (company_id) 
        company_id, 
        close_price as current_price
    FROM stock_prices
    ORDER BY company_id, price_date DESC
)
SELECT 
    p.user_name,
    SUM(h.quantity * lp.current_price) as total_portfolio_value
FROM portfolios p
JOIN holdings h ON p.portfolio_id = h.portfolio_id
JOIN latest_prices lp ON h.company_id = lp.company_id
WHERE p.user_name = 'Alice'
GROUP BY p.user_name;