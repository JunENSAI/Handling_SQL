-- Question 1

CREATE INDEX idx_film_title
ON film (title);

-- Question 2

CREATE INDEX idx_rental_inventory
ON rental (inventory_id, rental_date);