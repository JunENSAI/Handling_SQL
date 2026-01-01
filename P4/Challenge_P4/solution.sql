-- Question 1

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    signup_date TIMESTAMP DEFAULT NOW()
);

CREATE TABLE restaurants (
    rest_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    rating DECIMAL(2,1) CHECK (rating BETWEEN 0 AND 5)
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    rest_id INT REFERENCES restaurants(rest_id),
    total NUMERIC(5,2) CHECK (total > 0),
    status TEXT DEFAULT 'Pending' CHECK (status IN ('Pending', 'Delivered', 'Cancelled'))
);

-- Question 2

BEGIN;
INSERT INTO orders (user_id,rest_id,total) VALUES (1,5,50);
UPDATE users
SET last_active = NOW()
WHERE user_id = 1;
-- ROLLBACK;
COMMIT;

-- Question 3

CREATE INDEX idx_order_status
ON orders(user_id, status)


-- `user_id` is the most selective column (there are thousands of users, but only 3 statuses). Narrowing down to "User 99" first makes the list very short, then checking for "Delivered" is instant.

-- Question 4

INSERT INTO restaurant (rest_id,name,rating) VALUES (10,'Burger King', 3.5)
ON CONFLICT (rest_id)
DO UPDATE SET rating = 3.5;

-- Question 5

CREATE VIEW support_dashboard AS
SELECT
    ord.order_id,
    ord.user_id,
    resto.name,
    ord.total,
    ord.status
FROM orders as ord
JOIN restaurants resto on ord.rest_id = resto.rest_id
WHERE ord.status <> 'Delivered';
