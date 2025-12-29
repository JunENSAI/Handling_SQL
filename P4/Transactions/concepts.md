## 1. What is a Transaction?

A transaction is a **single unit of work**.
It bundles multiple SQL steps together. Either **ALL** of them happen, or **NONE** of them happen.

* **Example:** Transferring money from Alice to Bob.
    
    1. Subtract $100 from Alice.
   
    2. Add $100 to Bob.
    * *Crash Scenario:* If the power goes out after step 1 but before step 2, Alice loses money and Bob gets nothing. A Transaction prevents this.

---

## 2. ACID Properties

* **A - Atomicity:** All or Nothing.

* **C - Consistency:** The database remains valid (constraints are checked).

* **I - Isolation:** Transactions don't interfere with each other (until committed).

* **D - Durability:** Once saved, it survives a power outage.

---

## 3. The Commands

* `BEGIN;` Starts the transaction.

* `COMMIT;` Saves changes permanently.

* `ROLLBACK;` Undoes everything since `BEGIN`.

---

## 4. The Dangerous "Autocommit"

By default, most SQL clients (like DBeaver) are in "Autocommit" mode. Every single line you run is instantly committed.

You must explicitly use `BEGIN` to enter safety mode.

---