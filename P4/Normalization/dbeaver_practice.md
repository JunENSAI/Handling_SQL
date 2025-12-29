`NORMALIZATION`

**Database: Pagila**

```sql
-- 1. The Bad Table (Denormalized)
CREATE TABLE bad_orders (
    order_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_email VARCHAR(100), -- Redundant! Repeats for every order.
    product_name VARCHAR(100),
    supplier_name VARCHAR(100),
    supplier_phone VARCHAR(20)   -- Transitive! Depends on supplier, not order.
);

INSERT INTO bad_orders (customer_name, customer_email, product_name, supplier_name, supplier_phone)
VALUES 
('Alice', 'alice@test.com', 'Laptop', 'TechCorp', '555-0199'),
('Alice', 'alice@test.com', 'Mouse', 'TechCorp', '555-0199'),
('Bob', 'bob@test.com', 'Laptop', 'TechCorp', '555-0199');

-- PROBLEM: If TechCorp changes their phone number, we have to update 3 rows.
-- If we delete Bob's order, we might lose Bob's email info entirely.

-- 2. Fixing it (Normalization)

-- Step A: Extract Customers (3NF Fix)
CREATE TABLE norm_customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

-- Step B: Extract Suppliers (3NF Fix)
CREATE TABLE norm_suppliers (
    supplier_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
);

-- Step C: The Orders Table (Links them)
CREATE TABLE norm_orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES norm_customers(customer_id),
    supplier_id INT REFERENCES norm_suppliers(supplier_id),
    product_name VARCHAR(100)
);

-- Now, if TechCorp changes phone numbers, we update ONE row in norm_suppliers.
```