-- Question 1

BEGIN;
INSERT INTO my_bank (name, balance) VALUES ('Charlie', 0);
COMMIT;

-- Question 2

BEGIN;
UPDATE my_bank SET balance = balance + 1000 WHERE name = 'Charlie';
ROLLBACK; -- there is a mistake, we undo the update