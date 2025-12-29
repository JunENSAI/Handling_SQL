import pandas as pd

# Imagine this is our messy raw data
raw_data = {
    'customer': ['Alice', 'Alice', 'Bob'],
    'email': ['a@test.com', 'a@test.com', 'b@test.com'],
    'product': ['Laptop', 'Mouse', 'Laptop']
}

def normalize_data():
    df = pd.DataFrame(raw_data)
    print("--- Raw Data ---")
    print(df)
    
    # 1. Extract Unique Customers
    customers = df[['customer', 'email']].drop_duplicates().reset_index(drop=True)
    customers['customer_id'] = range(1, len(customers) + 1)
    
    print("\n--- Normalized Customers Table ---")
    print(customers)
    
    # 2. Map IDs back to the Orders
    orders = pd.merge(df, customers, on='email')
    
    # Select only the FK and the Product
    final_orders = orders[['customer_id', 'product']]
    
    print("\n--- Normalized Orders Table ---")
    print(final_orders)

if __name__ == "__main__":
    normalize_data()