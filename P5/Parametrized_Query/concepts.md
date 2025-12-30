## 1. The Threat: SQL Injection 
SQL Injection happens when a user tricks your database by inputting SQL commands instead of data.

**The Vulnerable Way (String Concatenation):**
Imagine you have this Python code using an f-string:
```python
user_input = 'Robert'; DROP TABLE users; --"
query = f"SELECT * FROM users WHERE name = '{user_input}'"
```

What the DB sees: `SELECT * FROM users WHERE name = 'Robert'; DROP TABLE users; --'`

- It finds Robert.

- It DELETES the users table.

- It comments out the rest (--).

---

## 2. The Solution: Parameterized Queries

Instead of gluing strings together, you use Placeholders. In psycopg2 (Postgres), the placeholder is %s.

The Safe Way:

```Python
query = "SELECT * FROM users WHERE name = %s"
cursor.execute(query, (user_input,))
```

**How it works:** 

- The database driver sends the SQL template ("SELECT...") and the data ("Robert...") separately.

- The database treats the input strictly as text data, never as executable code.

---

## 3. Important Syntax Rules

- Use `%s` for everything: Even for integers or dates. The driver handles the type conversion.

- No Quotes: Do not write '%s'. Just `%s`.

- Tuples: The second argument to .execute() must be a tuple/list.

    - Correct: (value,) (Note the comma for a single item tuple).

    - Incorrect: (value) (This is just a variable in parenthesis).

---