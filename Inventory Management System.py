# Initialize store inventory using lists and dictionaries
inventory = [
    {"id": 1, "name": "Mobile", "price": 500.0, "quantity": 50},
    {"id": 2, "name": "pencile", "price": 2.0, "quantity": 30},
    {"id": 3, "name": "Laptop", "price": 1000.0, "quantity": 40}
]

# Function to display the current inventory
def display_inventory():
    print("Current Inventory:")
    print("------------------")
    for product in inventory:
        print(f"ID: {product['id']}, Name: {product['name']}, Price: ${product['price']}, Quantity: {product['quantity']}")
    print("------------------")

# Function to add a new product to the inventory
def add_product(name, price, quantity):
    new_product = {
        "id": len(inventory) + 1,
        "name": name,
        "price": price,
        "quantity": quantity
    }
    inventory.append(new_product)
    print(f"{name} added to the inventory.")

# Function to process a transaction
def process_transaction(product_id, quantity):
    for product in inventory:
        if product["id"] == product_id:
            if product["quantity"] >= quantity:
                product["quantity"] -= quantity
                print(f"Transaction successful. {quantity} units of {product['name']} sold.")
            else:
                print("Insufficient stock.")
            return
    print("Product not found.")

# Main loop for the program
while True:
    print("\n1. Display Inventory\n2. Add Product\n3. Process Transaction\n4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        display_inventory()

    elif choice == '2':
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter initial quantity: "))
        add_product(name, price, quantity)

    elif choice == '3':
        display_inventory()
        product_id = int(input("Enter product ID to sell: "))
        quantity = int(input("Enter quantity to sell: "))
        process_transaction(product_id, quantity)

    elif choice == '4':
        print("Exiting program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
