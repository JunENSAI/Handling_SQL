CREATE OR REPLACE VIEW v_portfolio_performance AS
WITH latest_prices AS (
    SELECT DISTINCT ON (company_id) 
        company_id, 
        close_price as current_price
    FROM stock_prices
    ORDER BY company_id, price_date DESC
)
SELECT 
    p.user_name,
    c.company_name,
    h.quantity,
    h.purchase_price,
    lp.current_price,
    (lp.current_price - h.purchase_price) * h.quantity AS gain_loss
FROM portfolios p
JOIN holdings h ON p.portfolio_id = h.portfolio_id
JOIN companies c ON h.company_id = c.company_id
JOIN latest_prices lp ON h.company_id = lp.company_id;