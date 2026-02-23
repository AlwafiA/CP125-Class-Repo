def compare_prices(store_a, store_b):
    # Initialize our result dictionary with empty lists
    results = {
        "only_a": [],
        "a_cheaper": [],
        "b_cheaper": []
    }
    
    # We only care about products present in Store A
    for product, price_a in store_a.items():
        # Case 1: Product is NOT in Store B
        if product not in store_b:
            results["only_a"].append(product)
            
        else:
            price_b = store_b[product]
            
            # Case 2: Store A is strictly cheaper
            if price_a < price_b:
                results["a_cheaper"].append(product)
            
            # Case 3: Store B is strictly cheaper
            elif price_b < price_a:
                results["b_cheaper"].append(product)
            
            # Case 4: Prices are equal (Instructions say skip these)
            else:
                continue

    # Sort each list alphabetically before returning
    for key in results:
        results[key].sort()
        
    return results

# --- Testing the Example ---
store_a = {"milk": 3.50, "bread": 2.00, "eggs": 5.00, "butter": 4.50}
store_b = {"milk": 3.00, "bread": 2.50, "eggs": 5.00, "coffee": 8.00}

result = compare_prices(store_a, store_b)
print(result["only_a"])
print(result["a_cheaper"])
print(result["b_cheaper"])
