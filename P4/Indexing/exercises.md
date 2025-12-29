## Question 1

**Write a SQL statement to create an index named idx_film_title on the title column of the film table.**

```sql
CREATE INDEX idx_film_title
ON film (title);
```

## Question 2

We frequently run this query: `SELECT * FROM rental WHERE rental_date > '2005-01-01' AND inventory_id = 50;` 

**Write a SQL statement to create a Composite Index that optimizes this specific query.** Hint: Think about which column helps narrow down the search fastest. Usually Equality (=) goes before Range (>).

```sql
CREATE INDEX idx_rental_inventory
ON rental (inventory_id, rental_date);
```

## Question 3

You have an index on (last_name, first_name). Which of these queries will NOT use the index effectively?

- WHERE last_name = 'Smith'

- WHERE last_name = 'Smith' AND first_name = 'John'

- WHERE first_name = 'John'

**The last one, because you cannot find "John" in a customer sorted by Last Name without reading every single page. The index is useless here.**