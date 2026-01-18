# CP115 Assignment: discount_calculator
# Name: ALWAFI ABDULGADER ALAMIN
# Matric No: MC2515202741


selection = input("""=== COOPMART INVENTORY SYSTEM === \n1. Add item \n2. Delete item\n3. Search item\n4. Show inventory\n5. Exit\nEnter choice (1-5):""")

inventory = []
while selection != '5':

    if selection == '1':
        item = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        inventory.append([item, qty])
        print(f"Item '{item}' added.")

    elif selection == '2':
        item = input("Enter item name: ")
        found = False
        for inv_item in inventory:
            if inv_item[0] == item:
                inventory.remove(inv_item)
                found = True
                print(f"Item '{item}' removed.")
                break
        if not found:
            print(f"Item '{item}' not found in inventory.")

    elif selection == '4':
        print(inventory)
        
    selection = input("""=== COOPMART INVENTORY SYSTEM === \n1. Add item \n2. Delete item\n3. Search item\n4. Show inventory\n5. Exit\nEnter choice (1-5):""")