## Question 1

Create a table **employees** with:

- `id:` Serial PK.

- `salary:` Integer.

- Add a `CHECK constraint` to ensure salary is greater than 10,000.


## Question 2
Create a table **orders** with:

- `order_id`: Serial PK.

- `status`: Text.

- Add a `CHECK constraint` that forces status to be either 'Pending', 'Shipped', or 'Delivered'.

## Question 3

- Create a table **departments** (`dept_id` Serial PK, `dept_name` Text Unique).

- Create a table **staff_assignments** that has:

    - `assignment_id` Serial PK.

    - `dept_id` Integer.

    - `Foreign Key`: dept_id must reference departments(dept_id).

    - `Unique Constraint:` A combination of columns. Ensure that a staff member (use a dummy column staff_name for now) cannot be assigned to the same department twice.
