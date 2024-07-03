# Create two different lists and print all items using a  for loop
print("\nDrinks Lists")
tea = [ "chai", "matcha", "rooibos", "hibiscus", "chamomile" ]
cocktail = [ "margarita", "martini", "amaretto sour", "mojito", "daiquiri" ]
print("\nThe complete list.")
print(tea)
print(" ")
print(cocktail)

# Print a single items from each list
print("\nA single entry.")
print(tea [3])
print(cocktail[3])
print(" ")

# Add an item to each list
print("\nWith Added Items.")
tea.insert(0, "lemon")
print(tea, "\n")
cocktail.insert(0, "tom collins")
print(cocktail, "\n")

# Delete an item from each list
print("\nDelete an entry.")
del tea[3] 
print(tea, "\n")
del cocktail[3] 
print(cocktail, "\n")


# Concatenate the two lists and print
print("\nItems in list.")
print("You have", len(tea), "items in your tea box and", len(cocktail), "cocktails prepped.")
print("\nConcatenating two lists.")
drinks = tea + cocktail
print("Your drinks list now contains the following:")
for item in drinks:
	print(item)