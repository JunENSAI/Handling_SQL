--Q1 : Find the Top 10 customers based on the total amount of money they have paid.

SELECT 
    c.first_name,
    c.last_name,
    SUM(p.amount) AS total_spend
FROM customer c
INNER JOIN payment p 
    ON c.customer_id = p.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_spend DESC
LIMIT 10;

--Q2 : Find the titles of all films that do not exist in the inventory table.

SELECT 
    f.title,
    i.inventory_id
FROM film f
LEFT JOIN inventory i 
    ON f.film_id = i.film_id
WHERE i.inventory_id IS NULL;

--Q3 : List the Top 5 Countries by total revenue.

select
	co.country,
    SUM(p.amount) AS total_spend
from payment p
inner join customer c
	on p.customer_id  = c.customer_id
inner join address a
	on c.address_id  = a.address_id 
inner join city ci
	on a.city_id = ci.city_id 
inner join country co
	on ci.country_id = co.country_id 
GROUP BY co.country
ORDER BY total_spend DESC
limit 5;

--Q4 : List the category name and the total revenue, sorted by highest revenue.

select
	ca."name",
	SUM(p.amount) AS total_spend
from payment p
inner join rental r
	on p.rental_id = r.rental_id 
inner join inventory i
	on r.inventory_id = i.inventory_id 
inner join film_category fc 
	on i.film_id = fc.film_id
inner join category ca
	on fc.category_id = ca.category_id 
GROUP BY ca."name" 
ORDER BY total_spend desc;

-- Q5 : List the titles and lengths of all movies that are longer than the average length of all movies in the database.

SELECT 
    title, 
    length 
FROM film
WHERE length > (SELECT AVG(length) FROM film)
ORDER BY length desc;

-- Q6 : List the First Name and Last Name of the actors, along with the count of films they have appeared in. Sort by the most films to the least.

select a.first_name, a.last_name, count(fa.actor_id) as film_appeareance
from actor a
inner join film_actor fa
	on a.actor_id = fa.actor_id
GROUP BY a.actor_id, a.first_name , a.last_name 
order by film_appeareance desc;

-- Q7 : Which store has processed more total money?

select sum(p.amount) as total_money, s.store_id
from payment p
inner join staff s
	on p.staff_id = s.staff_id
GROUP BY s.store_id
ORDER BY total_money desc;
