### Question 1

**Use jsonb_build_object to create a JSON column for each actor containing their first_name and last_name. Alias the column as actor_json.**

```sql
SELECT 
    first_name,
    last_name,
    jsonb_build_object(
        'first_name', first_name, 
        'last_name', last_name, 
    ) as actor_json
FROM actor;
```

### Question 2

**Create a CTE that builds a JSON object for films (containing rating and length). Select from this CTE and filter for films where the JSON rating key is equal to 'R'.**

```sql
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
```

### Question 3

**The special_features column is an Array ['Trailers', 'Commentaries']. Find all films that have BOTH 'Trailers' AND 'Deleted Scenes'.**

```sql
SELECT 
    title,
    special_features
FROM film
WHERE special_features @> ARRAY['Trailers', 'Deleted Scenes'];
```