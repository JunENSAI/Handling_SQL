*Note: Assume you have a table products with columns id, name, price, stock.*

## Question 1

**Write a query to Insert a new product: "Shiny Widget", Price 100, Stock 50.**

```sql
INSERT INTO products (name,price,stock) VALUES ('Shiny Widget', 100,50)
```

## Question 2

**Write a query to Update the price of all products named "Shiny Widget". Increase their price by 10%.**

```sql
UPDATE products 
SET price = price * 1.1 
WHERE name = "Shiny Widget";
```

## Question 3

**Write a query to Insert a product with id = 99, name = 'Super Widget'. If ID 99 already exists, update the stock column by adding 10 to the existing stock count. **

```sql
INSERT INTO products (id,name) VALUES (99,'Super Widget')
ON CONFLICT (id)
DO UPDATE SET stock = products.stock + 10;
```