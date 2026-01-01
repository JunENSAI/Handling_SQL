## Question 1

You have 

- A table `students`: student_id, name, subjects_taken 

- Row: 1, 'John', 'Math, Science, History' 

**Which Normal Form is this violating? (1NF, 2NF, or 3NF)?**

- 1NF Rule: Columns must be "Atomic" (hold a single value).

- **The Violation:** The column subjects_taken contains 'Math, Science, History'. `This is a comma-separated list (multiple values in one cell).`

## Question 2

You have 

- A table `gym_visits`: visitor_id, gym_location, gym_address, visit_date (Assume visitor_id is the PK). 

- The gym_address depends on gym_location. If the location is "Downtown", the address is always "123 Main St". 

**Which Normal Form is this violating, and why?**

`3NF` becuase gym_adress (a non-key depends on another non-key column gym_location).

## Question 3

**Write the CREATE TABLE statements to normalize the gym_visits table from Question 2 into 3NF.**