`VIEWS`

**Database: Pagila**

```sql
-- 1. Create a Standard View
-- Let's create a "Master List" of customer details (Name + Address + City + Country).
CREATE OR REPLACE VIEW customer_master_list AS
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    c.email,
    a.address,
    ci.city,
    co.country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id;

-- 2. Query the View
-- Now it looks like a simple table!
SELECT * FROM customer_master_list
WHERE country = 'Japan';

-- 3. Create a Materialized View (Performance)
-- Let's calculate total revenue per Category.
CREATE MATERIALIZED VIEW category_revenue_mat AS
SELECT 
    c.name AS category_name,
    SUM(p.amount) AS total_revenue
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY c.name;

-- 4. Query it
SELECT * FROM category_revenue_mat;

-- 5. Refresh it
-- If we add new payments, this view won't change until we run:
REFRESH MATERIALIZED VIEW category_revenue_mat;

-- 6. Drop them
DROP VIEW customer_master_list;
DROP MATERIALIZED VIEW category_revenue_mat;
```