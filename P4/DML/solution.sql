-- Question 1

INSERT INTO products (name,price,stock) VALUES ('Shiny Widget', 100,50)

-- Question 2

UPDATE products 
SET price = price * 1.1 
WHERE name = "Shiny Widget";

-- Question 3

INSERT INTO products (id,name) VALUES (99,'Super Widget')
ON CONFLICT (id)
DO UPDATE SET stock = products.stock + 10;