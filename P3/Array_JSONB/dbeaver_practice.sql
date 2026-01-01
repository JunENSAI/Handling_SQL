-- JSONB : Pagila DB

-- 1. Creating JSON on the fly
-- Let's pretend we are building a JSON object from our film table.
SELECT 
    film_id,
    title,
    -- Build a JSON blob
    jsonb_build_object(
        'rating', rating, 
        'length', length, 
        'features', special_features
    ) as film_metadata
FROM film
LIMIT 5;

-- 2. Querying inside JSON (The Arrow Operator)
-- We will use a CTE to create fake JSON data, then query it.
WITH json_data AS (
    SELECT 
        film_id, 
        title,
        jsonb_build_object('rating', rating, 'cost', replacement_cost) as meta
    FROM film
)
SELECT 
    title,
    meta,
    (meta ->> 'cost')::numeric as price
FROM json_data
WHERE (meta ->> 'rating') = 'PG';

-- 3. Working with Arrays (Postgres specific)
-- The 'special_features' column in Pagila is actually an ARRAY type (text[]), not JSON.
-- Let's query it using Array operators.
SELECT 
    title,
    special_features
FROM film
WHERE 'Deleted Scenes' = ANY(special_features); 
-- logic: Is 'Deleted Scenes' inside the array?

-- 4. Unnesting (Exploding Arrays)
-- We want to count how many movies have "Trailers", how many have "Commentaries", etc.
SELECT 
    unnest(special_features) as feature,
    COUNT(*) as total_count
FROM film
GROUP BY feature
ORDER BY total_count DESC;
