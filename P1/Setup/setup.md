## 1. Objective

Before writing queries, we need a realistic dataset. We will use **Pagila**, the standard PostgreSQL sample database. It represents a DVD rental store (Customers, Films, Rentals, Payments) and is perfect for mastering complex joins and window functions.

---

## 2. Setting up the Database (Pagila)

### Step A: Get the Data

1. Open your browser and search for **"Postgres Pagila database sql"** or go to the official GitHub repository for postgres/pagila.

2. Download the file named `pagila-insert-data.sql` and `pagila-schema.sql` (or a combined `.sql` file if available).

### Step B: Create the Container in DBeaver

1. Open **DBeaver**.

2. Connect to your local PostgreSQL instance (usually `localhost:5432`).

3. Right-click on "Databases" -> **Create New Database**.

4. Name it `pagila`.

### Step C: Restore the Data

1. In DBeaver, right-click on your new `pagila` database.

2. Select **Tools** -> **Execute Script** (or open a SQL Editor).

3. Load the `pagila-schema.sql` first and run it (Alt+X or Ctrl+Enter).

4. Load the `pagila-insert-data.sql` second and run it.

* *Note: If you have a single `.backup` or `.tar` file, use "Tools -> Restore" instead.*

---

## 3. Python Environment Setup
We will use Python later to automate our SQL. We need three key libraries:

* **`psycopg2-binary`**: The driver that lets Python talk to Postgres.

* **`pandas`**: For data manipulation (Excel on steroids).

* **`sqlalchemy`**: For smoother database connections.

---

## 4. DBeaver Shortcut Keys

* **Ctrl + Enter**: Execute the statement under the cursor.

* **Ctrl + Space**: Auto-complete (table names, columns).

* **F3**: Open the detailed view of the table/object selected.

---