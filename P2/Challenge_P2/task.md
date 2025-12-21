**Scenario:** The CEO of the DVD Rental company wants a performance report. She has sent you 7 specific questions.

Question 1: The VIP List

- **The Ask:** We want to send a gift to our best customers. Find the Top 10 customers based on the total amount of money they have paid. Display their first name, last name, and total spend.

**Hint:** Tables: customer, payment. Columns: first_name, last_name, amount.

Question 2: The "Ghost" Movies

- **The Ask:** We have a catalog of films, but not all of them are actually in stock (in our inventory). Find the titles of all films that do not exist in the inventory table.

- **Hint:** Tables: film, inventory. Columns: title, film_id, inventory_id.

Question 3: Global Revenue

- **The Ask:** Which countries are we making the most money from? List the Top 5 Countries by total revenue.

- **Hint:** You will need to join 5 tables to link a payment back to a country.

- **Chain:** payment → customer → address → city → country.

Question 4: Category Champions

- **The Ask:** Which genre (Category) generates the most revenue? (e.g., Action, Comedy, Horror). List the category name and the total revenue, sorted by highest revenue.

- **Hint:** You need to link Payments to Categories.

- **Chain:** payment → rental → inventory → film_category → category.

Question 5: Above Average Films

- **The Ask:** List the titles and lengths of all movies that are longer than the average length of all movies in the database.

- **Hint:** Table: film. Columns: title, length. (Requires comparing a row to an aggregate).

Question 6: The Actor Count

- **The Ask:** We want to know which actors work the hardest. List the First Name and Last Name of the actors, along with the count of films they have appeared in. Sort by the most films to the least.

- **Hint:** Tables: actor, film_actor. Columns: first_name, last_name, actor_id.

Question 7: Store Wars

- **The Ask:** We have two stores (Store ID 1 and Store ID 2). Which store has processed more total money?

- **Hint:** The payment table records who processed the transaction (staff_id). The staff table links staff to a store_id.

- **Hint:** Tables: payment, staff. Columns: amount, store_id.