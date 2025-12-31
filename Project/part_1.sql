CREATE TABLE IF NOT EXISTS companies(
    company_id VARCHAR(10) PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    sector VARCHAR(50) NOT NULL
);


CREATE TABLE IF NOT EXISTS stock_prices (
    company_id VARCHAR(10) REFERENCES companies(company_id),
    price_date DATE,
    open_price DECIMAL(10, 2) CHECK(open_price >= 0),
    close_price DECIMAL(10, 2) CHECK(close_price >= 0),
    volume BIGINT,
    PRIMARY KEY (company_id, price_date)
);


CREATE TABLE IF NOT EXISTS portfolios (
    portfolio_id SERIAL PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS holdings (
    holding_id SERIAL PRIMARY KEY,
    portfolio_id INT REFERENCES portfolios(portfolio_id),
    company_id VARCHAR(10) REFERENCES companies(company_id),
    quantity INT CHECK (quantity > 0),
    purchase_price DECIMAL(10,2) CHECK (purchase_price >= 0),
    purchase_date DATE DEFAULT CURRENT_DATE
);