# List Methods
elements = []
menuChoice = None
while menuChoice != "0":
    print("\nElements Menu\n")
    print("0 = Exit")
    print("1 = Show Elements")
    print("2 = Add an Element")
    print("3 = Delete an Element")
    print("4 = Include Hidden Elements")
    print("5 = Show List")
    menuChoice = input("\nWhat do you want to do? ")

    # Create a list containing 5 or more elements
    if menuChoice == "1":
        print("\nList of Elements")
        elements = ["air", "geo", "electro", "earth", "hydro"]
        print("\nThe list.")
        print(elements)

    # Append new items
    elif menuChoice == "2":
        part = input("\nWhat would you like to add? ")
        elements.append(part)
        # Insert a new item in index position 3 (insert)
        if part == "random":
            elements.insert(3, "Celestial")
            print(elements)

    # Delete an item
    elif menuChoice == "3":
        part = input("\nWhich element would you like to remove? ")
        if part in elements:
            elements.remove(part)
        else:
            print("\nThat is not on the list.\a")

    # Create a new list with 3 items and append (extend)
    elif menuChoice == "4":
        otherList = ["pyro", "cryo", "gloom"]
        elements.extend(otherList)
        print(elements)

    # Sort list into ascending
    elif menuChoice == "5":
        listChoice = input("\n Would you like to see the order ascending or descending?")
        if listChoice == "ascending":
            elements.sort()
            print(elements)
        # and then into descending
        elif listChoice == "descending":
            elements.sort(reverse=True)
            print(elements)
