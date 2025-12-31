## Question 1: The Destination (SQL)

**The Task:** Write a SQL statement to create a table named `hr_employees` in Postgres. It must have these columns:

- emp_id (Integer, Primary Key)

- full_name (Text)

- salary (Integer)

- department (Text)

- is_high_earner (Boolean) - True if salary > 100,000

## Question 2 : The Cleaning Logic (Python)

**The Task:** The HR team sends salaries in this messy format: `"$120,000/yr", "$85k", " 50000 "`. Write a Python function called `clean_salary(value)` that takes a string and returns a clean Integer.

`Requirements:`

- Remove symbols like $, ,, /yr, and whitespace.

- If the string ends in 'k' (e.g., "85k"), multiply the number by 1000.

- Return the integer.

**Example Test Cases:**

- "$120,000/yr" -> 120000

- "85k" -> 85000

## Question 3

1. **Extract (Simulated):** Use this raw dictionary to create a Pandas DataFrame:

```Python
raw_data = {
    'id': [101, 102, 103],
    'name': ['Doe, John', 'Smith, Jane', 'Brown, Bob'],
    'raw_salary': ['$120,000/yr', '85k', ' $45,000 '],
    'dept': ['Engineering', 'Marketing', 'Sales']
}
```

2. **Transform:**

- Fix Names: The names are in "Last, First" format. Flip them to "First Last" (e.g., "John Doe").

- Fix Salaries: Apply your clean_salary function from Question 2 to the raw_salary column.

- Logic: Create the is_high_earner column (True if clean salary > 100,000).

3. **Load:**

- Use SQLAlchemy to load the transformed DataFrame into the hr_employees table you created in Question 1.

- Use if_exists='append' so we don't delete existing data.
