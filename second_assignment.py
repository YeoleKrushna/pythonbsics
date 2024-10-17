cart = []

while True:
    print("Shopping Cart System")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Display Cart")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))
        cart.append((item_name, quantity, price))

    elif choice == '2':
        item_name = input("Enter item name to remove: ")
        for item in cart:
            if item[0] == item_name:
                cart.remove(item)
                break
        else:
            print("Item not found in cart.")

    

    elif choice == '4':
        print("Exiting the system.")
        break

    else:
        print("Invalid choice. Please try again.")
