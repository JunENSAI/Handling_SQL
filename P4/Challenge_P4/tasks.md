## Question 1: From Mess to Normalized (DDL & Constraints)

**The Problem: The previous dev stored everything in raw_data (Customer Name, Restaurant Address, Order Status, etc.).** 

**The Task: Write the SQL to create 3 normalized tables (3NF) to replace this mess.**

1. Table `users`:

- **user_id**: Auto-incrementing PK.

- **email**: Text, Unique, Cannot be Null.

- **signup_date**: Timestamp, defaults to Now.

2. Table r`estaurants`:

- **rest_id**: Auto-incrementing PK.

- **name**: Text, Cannot be Null.

- **rating**: Decimal (e.g., 4.5), Check that it is between 0 and 5.

3. Table `orders`:

- **order_id**: Auto-incrementing PK.

- **user_id**: FK linking to users.

- **rest_id**: FK linking to restaurants.

- **total**: Numeric, Check that it is greater than 0.

- **status**: Text, Default 'Pending', Check that it is one of ('Pending', 'Delivered', 'Cancelled').


## Quuestion 2 : The Critical Transaction (DML & ACID)

**The Problem: A user (User ID 1) is ordering $50 worth of sushi from "Sushi Palace" (Restaurant ID 5).** 

**The Task: Write a Single Transaction (BEGIN...COMMIT) that does the following:**

* Inserts the new record into orders.

* Updates the users table to update their last_active column to NOW() (Assume this column exists).

* Constraint: If anything fails during these steps, the whole thing should roll back automatically (you don't need to write the rollback logic, just wrapping it in BEGIN/COMMIT is enough for this exercise).

## Question 3 : Performance Tuning (Indexing)

**The Problem:** The marketing team keeps running this slow query: `SELECT * FROM orders WHERE user_id = 99 AND status = 'Delivered';` 

**The Task: Write the SQL to create the optimal index for this specific query. Explain why you chose the column order.**

## Question 4 : The Upsert (Data Maintenance)

**The Problem: We are syncing data from a third-party partner. We receive a list of restaurants.** 

**The Task: Write a query to Insert a restaurant:**

- ID: 10

- Name: "Burger King"

- Rating: 3.5 Logic: If ID 10 already exists, do not error out. Instead, update the existing row's rating to be 3.5. 


## Question 5 : The Security View

**The Problem: We want to give a dashboard to our Customer Support agents, but we do not want them to see the user's private email or the restaurant's internal ID.** 

**The Task: Create a View called support_dashboard that shows:**

- Order ID

- User ID

- Restaurant Name (Not ID)

- Order Total

- Order Status

- Filter: Show only orders that are NOT 'Delivered' (we only care about active issues).
