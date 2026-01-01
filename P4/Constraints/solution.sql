-- Question 1

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    salary INTEGER CHECK (salary > 10000)
);

-- Question 2

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    status TEXT CHECK (status in ('Pending','Shipped','Delivered'))
);

-- Question 3

CREATE TABLE departments (
    dept_id SERIAL PRIMARY KEY,
    dept_name TEXT UNIQUE
);

CREATE TABLE staff_assignments (
    assignment_id SERIAL PRIMARY KEY,
    dept_id INTEGER REFERENCES departments(dept_id),
    staff_name VARCHAR(50),
    UNIQUE(staff_name, dept_id)
);