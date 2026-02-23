def apply_upgrade(current, upgrade):
    """
    Applies an upgrade batch to permissions, ensuring levels only increase.
    """
    # Create a new dictionary to avoid modifying the original 'current'
    final_permissions = current.copy()
    
    for permission, new_level in upgrade.items():
        # Check if the permission is already in our dictionary
        if permission in final_permissions:
            # If the new level is higher, update it
            if new_level > final_permissions[permission]:
                final_permissions[permission] = new_level
            # If it's lower or equal, the 'if' condition fails and we keep the current level
        
        else:
            # If the permission doesn't exist, always add it
            final_permissions[permission] = new_level
            
    return final_permissions

# --- Testing the Example ---
current = {"read": 2, "write": 1, "admin": 0}
upgrade = {"read": 1, "write": 3, "execute": 2}

result = apply_upgrade(current, upgrade)
print(result)
# Output: {'read': 2, 'write': 3, 'admin': 0, 'execute': 2}

current = {"read": 2, "write": 1, "admin": 0}
upgrade = {"read": 1, "write": 3, "execute": 2}
result = apply_upgrade(current, upgrade)
print(result)
print(current)   # Should be unchanged
