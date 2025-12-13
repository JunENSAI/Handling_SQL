## 1. The Declarative Paradigm

Unlike Python, where you tell the computer *how* to do things (loops, variables), SQL is **Declarative**. You tell the database *what* you want, and the database engine's "Optimizer" figures out the most efficient way to get it.

---

## 2. The Big Four Keywords

### A. SELECT (Projection)

* **Math Concept:** In Relational Algebra, this is called **Projection** ($\pi$).

* **Function:** It chooses which **columns** (attributes) to return.

* **Wildcard:** `SELECT *` returns all columns. (Note: Avoid using `*` in production code; it slows down the network and breaks applications if table structures change).

### B. FROM (Data Source)

* **Function:** Specifies the **table** (relation) to query.

* **Crucial Rule:** The database looks at the `FROM` clause *before* the `SELECT` clause. It needs to find the file cabinet before it can pull the files.

### C. DISTINCT (Set Theory)
* **Function:** Removes duplicate rows.

* **Math Concept:** In a strict mathematical "Set", duplicates are not allowed $\{1, 2, 2\}$ is effectively $\{1, 2\}$. SQL tables are "Multisets" (duplicates allowed) until you force uniqueness with `DISTINCT`.

### D. LIMIT (Cardinality Constraint)
* **Function:** Restricts the number of rows returned.

* **Use Case:** Always use this when exploring a new table to avoid crashing your DBeaver with 10 million rows.

---

## 3. Order of Execution (Mental Model)

When you run the code below:

```sql
SELECT DISTINCT first_name 
FROM actor 
LIMIT 5;
```

The Database Engine thinks in this order:

- `FROM actor`: "Go to the hard drive, find the actor table."

- `SELECT`: "Grab only the first_name column."

- `DISTINCT`: "Remove any duplicates from this list."

- `LIMIT`: "Cut it off after the first 5 results."

---