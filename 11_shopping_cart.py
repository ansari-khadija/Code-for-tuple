# 11 - Real-Life Tuple Application
# Shopping Cart System

print("===== SHOPPING CART =====")

# Product information stored as tuples
product1 = ("Laptop", 55000, 1)
product2 = ("Mouse", 800, 2)
product3 = ("Keyboard", 1500, 1)

# Shopping cart containing multiple product tuples
cart = (product1, product2, product3)

print("\n--- Products in Cart ---")

for product in cart:
    print("Product:", product[0])
    print("Price:", product[1])
    print("Quantity:", product[2])
    print()

# Calculating total price
total = 0

for product in cart:
    price = product[1]
    quantity = product[2]

    total = total + (price * quantity)

print("--- Bill Summary ---")
print("Number of products:", len(cart))
print("Total Amount: ₹", total)

# Displaying first and last product
print("\n--- Cart Details ---")
print("First product:", cart[0][0])
print("Last product:", cart[-1][0])

# Slicing the cart
print("First two products:", cart[:2])

# Checking whether a product exists
print("\n--- Product Search ---")

print("Laptop in cart:", "Laptop" in cart[0])
print("Mouse in cart:", "Mouse" in cart[1])

# Final cart
print("\n--- Final Cart ---")
print(cart)
