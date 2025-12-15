
## 1. The Email Campaign

We need a list of all customer email addresses, but we need them to be in lowercase and sorted alphabetically.

---

## 2. The Content Review

Find all films that are rated 'PG-13' but are longer than 3 hours (180 minutes). Return the title and length.

---

## 3. The Lost Payments
 
Find the payment IDs and amounts for all payments that were $0.00. (We need to investigate these).

---

## 4. The Late Night Rentals

Find the rental IDs and rental dates for all rentals that happened after 10:00 PM (22:00:00) on any day. (Hint: Use EXTRACT(HOUR FROM ...)).

---

## 5. The Replacement Cost 

We are auditing our inventory. Find the top 5 most expensive movies to replace (replacement_cost). If there is a tie, sort by the movie title alphabetically.

---

## 6. The "B" Movies 

Find all movies that have "Boat" or "Beautiful" in the title. (Hint: Use OR with LIKE).

---

## 7. The Weekend Watch 

Find all rentals that occurred on a Sunday in May 2005. (Hint: Use EXTRACT(DOW ...) where 0 is Sunday, and EXTRACT(MONTH ...)).

---

## 8. The Short Description

Return the first_name of the actor and the first 10 characters of their last_name (in case they have a very long name), formatted as: "Name: [First] [First 10 of Last]".

---

## 9. The Privacy Check 

Find all customers who do not have an active status (active = 0) OR whose email is NULL.

---

## 10. The "New" Classics 

Find movies released in 2006 that have a rental rate less than 1.50 AND a rating of either 'G' or 'PG'.

---