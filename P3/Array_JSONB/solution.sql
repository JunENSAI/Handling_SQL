-- Question 1

SELECT 
    first_name,
    last_name,
    jsonb_build_object(
        'first_name', first_name, 
        'last_name', last_name, 
    ) as actor_json
FROM actor;

-- Question 2

WITH json_rating AS (
    SELECT 
        rating, 
        length,
        jsonb_build_object('rating', rating, 'length', length) as meta_rating
    FROM film
)
SELECT 
    rating,
    length
FROM json_rating
WHERE (meta_rating ->> 'rating') = 'R'
ORDER BY length DESC;

-- Question 3

SELECT 
    title,
    special_features
FROM film
WHERE special_features @> ARRAY['Trailers', 'Deleted Scenes'];