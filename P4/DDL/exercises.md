## Question 1 

Write a SQL statement to create a table named **student_scores**. It should have:

- `student_id (Integer)`

- `subject (Text)`

- `score (Integer)`

```sql
CREATE TABLE student_scores (
    student_id INTEGER PRIMARY KEY,
    subject TEXT,
    score INTEGER
);
```


## Question 2 

Create a table named **marketing_leads**.

- `lead_id`: An auto-incrementing integer (SERIAL).

- `email`: Text, cannot be empty (NOT NULL).

- `is_contacted`: Boolean, defaults to FALSE.

- `signup_date`: Timestamp, defaults to the current time.

```sql
CREATE TABLE marketing_leads (
    lead_id SERIAL PRIMARY KEY,
    email TEXT NOT NULL,
    is_contacted BOOLEAN DEFAULT FALSE,
    signup_date TIMESTAMP DEFAULT NOW()
);
```

## Question 3

- Write an ALTER statement to add a column source (Text) (Table : marketing_leads).

- Write an ALTER statement to rename the column score in your student_scores table to final_grade.

```sql
ALTER TABLE marketing_leads ADD source TEXT;
```

```sql
ALTER TABLE student_scores RENAME COLUMN score TO final_grade;
```