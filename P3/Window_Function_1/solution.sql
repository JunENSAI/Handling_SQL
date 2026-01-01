-- Question 1

SELECT 
    *,
    ROW_NUMBER() OVER (ORDER BY title ASC) as row_num
FROM film;

-- Question 2

SELECT 
    title,
    rating,
    length,
    DENSE_RANK() OVER (PARTITION BY rating ORDER BY length DESC) as rank_in_rating
FROM film
ORDER BY length DESC;

-- Question 3

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