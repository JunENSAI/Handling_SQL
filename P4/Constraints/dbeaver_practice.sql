-- CONSTRAINTS : Pagila DB

-- 1. Create the Parent Table (Authors)
CREATE TABLE my_authors (
    author_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE -- Constraint: No duplicate emails
);

-- 2. Create the Child Table (Books)
CREATE TABLE my_books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    price NUMERIC(5, 2) CHECK (price > 0), -- Constraint: Price must be positive
    author_id INT REFERENCES my_authors(author_id) -- The Foreign Key
);

-- 3. Testing Valid Data
INSERT INTO my_authors (name, email) VALUES ('JK Rowling', 'jk@p.com');
INSERT INTO my_books (title, price, author_id) VALUES ('Harry Potter', 19.99, 1);

-- 4. Testing The Constraints (These should FAIL)

-- Test A: Duplicate Email
-- INSERT INTO my_authors (name, email) VALUES ('Fake JK', 'jk@p.com'); 
-- Error: duplicate key value violates unique constraint

-- Test B: Negative Price
-- INSERT INTO my_books (title, price, author_id) VALUES ('Bad Book', -5.00, 1);
-- Error: violates check constraint "my_books_price_check"

-- Test C: (Foreign Key)
-- Trying to add a book for Author ID 999 (who doesn't exist).
-- INSERT INTO my_books (title, price, author_id) VALUES ('Ghost Book', 10.00, 999);
-- Error: insert or update on table "my_books" violates foreign key constraint
