-- Question 1

CREATE TABLE student_scores (
    student_id INTEGER PRIMARY KEY,
    subject TEXT,
    score INTEGER
);

-- Question 2

CREATE TABLE marketing_leads (
    lead_id SERIAL PRIMARY KEY,
    email TEXT NOT NULL,
    is_contacted BOOLEAN DEFAULT FALSE,
    signup_date TIMESTAMP DEFAULT NOW()
);

-- Question 3

ALTER TABLE marketing_leads ADD source TEXT;

ALTER TABLE student_scores RENAME COLUMN score TO final_grade;