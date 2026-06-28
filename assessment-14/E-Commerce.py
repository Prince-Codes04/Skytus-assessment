products = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Mouse": 500,
    "Keyboard": 1000
}

cart = []

while True:
    print("\n===== PRODUCTS =====")

    for item, price in products.items():
        print(item, "-", price)

    print("\n1. Add Product")
    print("2. View Cart")
    print("3. Checkout")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product = input("Enter product name: ")

        if product in products:
            cart.append(product)
            print("Added to cart.")
        else:
            print("Product not available.")

    elif choice == "2":
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            total = 0
            print("\nYour Cart:")

            for item in cart:
                print(item, "-", products[item])
                total += products[item]

            print("Total =", total)

    elif choice == "3":
        total = 0

        for item in cart:
            total += products[item]

        print("Total Bill =", total)
        print("Thank you for shopping!")

        cart.clear()

    elif choice == "4":
        print("Visit Again!")
        break

    else:
        print("Invalid Choice.")