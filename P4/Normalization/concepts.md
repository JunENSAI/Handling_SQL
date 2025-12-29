## 1. The Goal

Bad databases store duplicate data (e.g., storing the Customer's address again for every single payment they make).

**Normalization** splits big tables into smaller, linked tables to eliminate duplication.

---

## 2. First Normal Form (1NF) - "Atomic"

* **Rule:** One value per cell. No lists or comma-separated strings.

* **Violation:** `("John", "Movies: Matrix, Titanic")`

* **Fix:** Split into rows or a separate table.

---

## 3. Second Normal Form (2NF) - "The Whole Key"

* **Rule:** Every column must depend on the **entire** Primary Key. (Only matters if you have a Composite Primary Key).

* **Violation:** Table `(Student, Course, Professor)`.

    * Key is `(Student, Course)`.

    * `Professor` depends only on `Course`, not on `Student`.

* **Fix:** Move `Professor` to a `Course` table.

---

## 4. Third Normal Form (3NF) - "Nothing but the Key"

* **Rule:** Non-key columns should not depend on other non-key columns (Transitive Dependency).

* **Violation:** Table `(Order_ID, Product_ID, Product_Price)`.

    * `Product_Price` depends on `Product_ID`, not the `Order_ID`.

    * If you update the price in one order, you have inconsistent prices elsewhere.

* **Fix:** Move `Price` to a `Products` table.

---

## 5. Summary Quote

"Every non-key attribute must provide a fact about the Key, the Whole Key, and Nothing But the Key, so help me Codd." (E.F. Codd invented the relational model).

---