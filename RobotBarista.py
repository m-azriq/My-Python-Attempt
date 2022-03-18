#Build a robot barista!!
print("Hello, welcome to Breakfast House.")
name = input("What is your name?\n")
print("Thank you so much for coming, " + name + ".\n\n\n")
menu = "1) Espresso.\n2) Latte. \n3) Americano. \n4) Mocha."
print(name + ", what would you like to have today? Here is our menu.\n" + menu)
order = input()
price = 8
quantity = input("How many cups of " + order + " would you like?\n")
total = price * int(quantity)
print("Your total is RM" + str(total) + ".")

#print("Sounds good. Please be seated, " + name + ". Your " + order + " will be ready in a moment.")