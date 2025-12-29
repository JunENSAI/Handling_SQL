`INDEXING`

**Database: Pagila**

```sql
-- 1. The Baseline (No Index)
-- Let's search for payments by a specific amount.
EXPLAIN ANALYZE
SELECT * FROM payment 
WHERE amount = 0.99;

-- 2. Create the Index
CREATE INDEX idx_payment_amount 
ON payment (amount);

-- 3. The Result (Index Scan)
-- Run the exact same query's Explain Analyze again.
EXPLAIN ANALYZE
SELECT * FROM payment 
WHERE amount = 0.99;

-- 4. Multi-Column Indexes (Composite)
-- If we often search by Customer AND Payment Date together.
CREATE INDEX idx_customer_date 
ON payment (customer_id, payment_date);

-- This optimizes: WHERE customer_id = 1 AND payment_date > '2020-01-01'
-- It usually does NOT optimize: WHERE payment_date > '2020-01-01' (Order matters!)

-- 5. Cleanup
DROP INDEX idx_payment_amount;
DROP INDEX idx_customer_date;
```