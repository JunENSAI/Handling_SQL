## Question 1 

Write a SQL statement to create a table named **student_scores**. It should have:

- `student_id (Integer)`

- `subject (Text)`

- `score (Integer)`

## Question 2 

Create a table named **marketing_leads**.

- `lead_id`: An auto-incrementing integer (SERIAL).

- `email`: Text, cannot be empty (NOT NULL).

- `is_contacted`: Boolean, defaults to FALSE.

- `signup_date`: Timestamp, defaults to the current time.

## Question 3

- Write an ALTER statement to add a column source (Text) (Table : marketing_leads).

- Write an ALTER statement to rename the column score in your student_scores table to final_grade.