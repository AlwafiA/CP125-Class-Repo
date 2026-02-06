# CP115 Assignment: discount_calculator
# Name: ALWAFI ABDULGADER ALAMIN
# Matric No: MC2515202741

inventory = {}

#define functions
def add_item():
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))

    if quantity < 0:
        print("Error: Quantity cannot be negative.")
        return
    if item in inventory:
        inventory[item] += quantity
        print(f"Item '{item}' already exists. Quantity updated to {inventory[item]}.")
    else:
        inventory[item] = quantity
        print(f"Item '{item}' added.")

def delete_item():
    item = input("Enter item name: ")
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")
    else:
        del inventory[item]
        print(f"Item '{item}' removed.")

def search_item():
    item = input("Enter item name: ")
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")
    else:
        print(f"Quantity of '{item}': {inventory[item]}")

def show_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Inventory:")
        for item, qty in inventory.items():
            print(f"{item}  {qty}")

print("== COOPMART INVENTORY SYSTEM === \n1. Add item \n2. Delete item\n3. Search item\n4. Show inventory\n5. Exit")
choice = int(input("Enter choice (1-5): "))
while choice != 5:
    if choice == 1:
        add_item()
    elif choice == 2:
        delete_item()
    elif choice == 3:
        search_item()
    elif choice == 4:
        show_inventory()
    else:
        print("Error: Invalid choice. Please enter a number between 1 and 5.")
    choice = int(input("Enter choice (1-5): "))
print("Goodbye!")

