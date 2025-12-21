## 1. The Concept

While an `INNER JOIN` discards rows that don't match, an **Outer Join** keeps them and fills the missing side with `NULL`.

### A. LEFT JOIN (The Standard)

* **Logic:** "Keep **everything** from the Left table (the first one mentioned). If you find a match in the Right table, attach it. If not, attach NULLs."

* **Use Case:** "Show me all Customers, and their payments if they have any." (If a customer has no payments, they still show up).

### B. RIGHT JOIN

* **Logic:** "Keep everything from the Right table."

* **Reality:** almost never used. It’s cleaner to just flip the tables and use a `LEFT JOIN`.

### C. FULL OUTER JOIN

* **Logic:** "Keep everything from **BOTH** sides."

* **Use Case:** Comparing two lists to see what is unique to each list and what overlaps.

---

## 2. The "Anti-Join" Pattern (Crucial Skill)

This is the most powerful use of a Left Join. It answers questions like "Which users have **never** bought anything?"

**The Recipe:**

1.  **LEFT JOIN** the tables.

2.  **WHERE** the Right Table's ID **IS NULL**.

*Logic:* If the Right Table returns NULL, it means the `JOIN` failed to find a match. Therefore, the record exists only in the Left table.

---