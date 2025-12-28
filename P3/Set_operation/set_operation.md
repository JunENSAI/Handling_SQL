## 1. Vertical vs Horizontal

* **Joins** combine tables **Horizontally** (adding columns).

* **Sets** combine tables **Vertically** (adding rows).

* *Rule:* To use Set Operations, both queries must have the **exact same number of columns** and compatible data types.

---

## 2. UNION vs UNION ALL

* **UNION:** Stacks the results and **removes duplicates**.

    * *Analogy:* Dumping two buckets of sand into one and sifting it.

* **UNION ALL:** Stacks the results and **keeps duplicates**.

    * *Analogy:* Just dumping the buckets. (Faster because it doesn't have to sort/check for duplicates).

---

## 3. INTERSECT

Returns only the rows that appear in **BOTH** result sets.

* *Math:* $A \cap B$

* *Use Case:* "Find customers who are Actors." (If you have a customer table and an actor table with First/Last names).

---

## 4. EXCEPT (or MINUS)

Returns rows that are in the **First** result set but **NOT** in the Second.

* *Math:* $A - B$

* *Use Case:* "Find films that are in the database but have NEVER been rented." (Alternative to the `LEFT JOIN ... IS NULL` pattern we learned on P2).

---