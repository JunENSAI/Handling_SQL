from sqlalchemy import create_engine, text

DB_URL = 'postgresql://postgres:db_password@localhost:5432/pagila'
engine = create_engine(DB_URL, echo=True)

def call_stored_function():
    print("--- Calling Postgres Function via SQLAlchemy ---")
    
    with engine.connect() as conn:
        query = text("SELECT calculate_late_fee(:ret, :rent, :dur)")
        
        params = {
            "ret": '2023-01-10', 
            "rent": '2023-01-01', 
            "dur": 5
        }
        
        result = conn.execute(query, params)

        fee = result.scalar()
        
        print(f"Calculated Late Fee: ${fee}")

if __name__ == "__main__":
    call_stored_function()