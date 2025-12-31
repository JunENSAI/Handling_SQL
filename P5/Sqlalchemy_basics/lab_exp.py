from sqlalchemy import create_engine, text, inspect

DB_URL = 'postgresql://postgres:db_password@localhost:5432/pagila'

engine = create_engine(DB_URL, echo=True) 
# echo=True prints the generated SQL to the console (great for debugging)

def core_example():
    print("\n--- SQLAlchemy Core (Raw SQL) ---")
    
    # We use a context manager (with...) so connections close automatically
    with engine.connect() as connection:
        # We must wrap strings in text()
        query = text("SELECT title, length FROM film WHERE length < :x")
        
        # We pass parameters safely using a dictionary
        result = connection.execute(query, {"x": 50})
        
        for row in result:
            # We can access columns by name (row.title) instead of index (row[0])
            print(f"Movie: {row.title} (Duration: {row.length})")

def inspect_db():
    inspector = inspect(engine)
    print(inspector.get_table_names())



if __name__ == "__main__":
    core_example()
    inspect_db()