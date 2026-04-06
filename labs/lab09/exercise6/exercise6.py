import pandas as pd

def critical_inventory(filename):
    # Load the inventory data
    df = pd.read_csv(filename)
    
    # 1. Total products is simply the number of rows in the CSV
    total_products = len(df)
    
    # 2. Filter for critical status: 
    # Stock < Reorder_Threshold AND Days_Since_Restock > 30
    critical_mask = (df['Stock'] < df['Reorder_Threshold']) & (df['Days_Since_Restock'] > 30)
    critical_df = df[critical_mask]
    
    # 3. Extract the count and the set of names
    critical_count = len(critical_df)
    critical_products = set(critical_df['Product_Name'])
    
    # Return the dictionary exactly as the tests expect
    return {
        "total_products": total_products,
        "critical_count": critical_count,
        "critical_products": critical_products
    }

if __name__ == "__main__":
    result = critical_inventory("labs\lab09\data\inventory.csv")
    print(result)