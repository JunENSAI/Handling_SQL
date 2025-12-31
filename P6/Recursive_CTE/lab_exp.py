import pandas as pd
from sqlalchemy import create_engine

DB_URL = 'postgresql://postgres:db_password@localhost:5432/pagila'
engine = create_engine(DB_URL)

def visualize_tree():
    query = """
    WITH RECURSIVE hierarchy AS (
        SELECT emp_id, name, manager_id, 0 as level
        FROM company_org
        WHERE manager_id IS NULL 
        
        UNION ALL
        
        SELECT e.emp_id, e.name, e.manager_id, h.level + 1
        FROM company_org e
        JOIN hierarchy h ON e.manager_id = h.emp_id
    )
    SELECT name, level FROM hierarchy ORDER BY level, manager_id;
    """
    
    df = pd.read_sql(query, engine)
    
    print("--- Org Chart ---")
    for index, row in df.iterrows():
        indent = "    " * row['level']
        print(f"{indent}|- {row['name']}")

if __name__ == "__main__":
    visualize_tree()