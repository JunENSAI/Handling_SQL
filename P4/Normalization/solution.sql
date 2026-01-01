-- Question 3

CREATE TABLE gym (
    gym_location VARCHAR(50) PRIMARY KEY,
    gym_adress VARCHAR(50)
);

CREATE TABLE visit(
    visitor_id SERIAL PRIMARY KEY,
    visit_date DATE,
    gym_location VARCHAR(50) REFERENCES gym(gym_location)
);

