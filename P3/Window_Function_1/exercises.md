### Question 1

**Write a query to list all films. Add a column called row_num that numbers the rows 1, 2, 3... sorted alphabetically by title**
```sql
SELECT 
    *,
    ROW_NUMBER() OVER (ORDER BY title ASC) as row_num
FROM film
```

### Question 2

*We want to see the longest movies for each rating category (G, PG, etc.).*

**Write a query that lists title, rating, length, and a new column rank_in_rating that ranks the movies by length (longest first) within their own rating. Use DENSE_RANK.**

```sql
SELECT 
    title,
    rating,
    length,
    DENSE_RANK() OVER (PARTITION BY rating ORDER BY length DESC) as rank_in_rating
FROM film
ORDER BY length DESC;
```

### Question 3

**Find the "Top 3" customers who have spent the most money. (affected with number 1,2,3)**

```sql
WITH customer_stats AS (
    SELECT customer_id, SUM(amount) as total_spend
    FROM payment
    GROUP BY customer_id
),
ranked_stats AS (
    SELECT 
        customer_id, 
        total_spend,
        RANK() OVER (ORDER BY total_spend DESC) as rank_val
    FROM customer_stats
)
SELECT * FROM ranked_stats 
WHERE rank_val <= 3;
```