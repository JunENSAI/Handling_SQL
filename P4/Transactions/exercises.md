## Question 1

Write the SQL commands to:

- Start a transaction.

- Insert a new user 'Charlie' into my_bank with 0 balance.

- Save the changes permanently.

```sql
BEGIN;
INSERT INTO my_bank (name, balance) VALUES ('Charlie', 0);
COMMIT;
```

## Question 2

Write the SQL commands to:

- Start a transaction.

- Update 'Charlie's balance to 5000.

- Realize that is a mistake.

- Undo the update so Charlie goes back to 0.

```sql
BEGIN;
UPDATE my_bank SET balance = balance + 1000 WHERE name = 'Charlie';
ROLLBACK; -- there is a mistake, we undo the update
```

## Question 3

You run:

```SQL

BEGIN;
UPDATE my_bank SET balance = 0 WHERE name = 'Alice';
-- You do NOT run COMMIT yet.
```
Then, you open a second DBeaver window (a new connection) and run: `SELECT * FROM my_bank WHERE name = 'Alice';`

What balance will the second window see?

* 0

* The original balance (e.g., 900)

* The query will freeze/hang.

Becuase of the I in ACID properties, the value of the balance remains the original balance (900). The action is isolated before any `COMMIT`.