# Games and Release Dates Dictionary
Game = {"1998" : "Spyro", "2017" : "Legend of Zelda-Breath of the Wild",
			"2009" : "Assassins Creed Renaissance ", "2023" : "Baldurs Gate",
			"2021" : "Omori", "2000" : "Final Fantasy 9" }
print("\nRelease Dates of Popular Games.\n")
for term in Game:
	definition = Game[term]
	print(term, "\b:", definition)
choice = None
while choice != "0":
	print("\nGames History Menu\n")
	print("0 = Exit")
	print("1 = Print Dictionary")
	print("2 = Look Up Year of Release")
	print("3 = Add A New Game")
	print("4 = Amend A Released Game and Date")
	print("5 = Delete A Game")
	choice = input("\nEnter your selection: ")
	# Exit
	if choice == "0":
		print("\nThank You!")
	# Print dictionary
	elif choice == "1":
		print("\nThe Games History Dictionary.\n")
		for term in Game:
			definition = Game[term]
			print(term, "\b:", definition)
	# Look up Game released same year
	elif choice == "2":
		year = input("\nEnter the year: ")
		if year in Game:
			print("\nOur noted Game released on", year, "is:", Game.get(year))
		else:
			print("\nInvalid Entry.")
	# Add
	elif choice == "3":
		newYear = input("\nEnter a year: ")
		if newYear not in Game:
			gameDesc = input("\nWhat Game was released that year?: ")
			Game[year] = gameDesc
			print("\nGame is added to dictionary.\n")
		else:
			print("\nThis already exists!")
	# Amend
	elif choice == "4":
		year = input("\nEnter the Year: ")
		if year in Game:
			new = input("\nEnter the amended Game: ")
			Game[year] = new
			print("\nThe entry has been changed.")
		else:
			print("\nInvalid Entry.")
	# Delete
	elif choice == "5":
		year = input("\nEnter year to delete: ")
		if year in Game:
			del Game[year]
			print("\nThe entry has been deleted.")
		else:
			print("\nInvalid Entry.")
	# Invalid selection
	else:
		print("\nInvalid selection!=")