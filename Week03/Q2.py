#Question 2: Shopping Car(Lists - Searching and Removal)
cart = ["apple", "milk", "banana"]
print("we have", cart.count("apple"), "apples")
print("The milk position", cart.index("milk"))
cart.remove("apple")
print("Removed item using pop", cart.pop())
print("Is banana in the cart?","banana"in cart)
print("Final cart: ",cart )