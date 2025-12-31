--PL/pgSQL : Pagila DB

-- 1. Create a Simple Calculation Function
-- We want a standard way to calculate late fees: $1.00 per day late.
CREATE OR REPLACE FUNCTION calculate_late_fee(return_date TIMESTAMP, rental_date TIMESTAMP, duration INT)
RETURNS NUMERIC AS $$
DECLARE
    actual_duration INT;
    late_days INT;
    fee NUMERIC;
BEGIN
    -- 1. Calculate how long they actually kept it (in days)
    -- EXTRACT(EPOCH...) gives seconds, divide by 86400 for days.
    actual_duration := EXTRACT(DAY FROM (return_date - rental_date));
    
    -- 2. Logic
    IF actual_duration <= duration THEN
        RETURN 0.00;
    ELSE
        late_days := actual_duration - duration;
        fee := late_days * 1.00;
        RETURN fee;
    END IF;
END;
$$ LANGUAGE plpgsql;

-- 2. Test it
-- Imagine a movie rented for 3 days, returned after 5 days.
SELECT calculate_late_fee('2023-01-05', '2023-01-01', 3);
-- Result should be 2.00

-- 3. Use it in a Query
-- Let's apply this to the real rental table (using constants for missing data for simplicity)
SELECT 
    rental_id, 
    calculate_late_fee(return_date, rental_date, 5) as potential_fee
FROM rental
WHERE return_date IS NOT NULL
LIMIT 5;