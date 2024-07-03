family = [("10.07.1991", "Bex", "Purple", "Both"), ("27.06.1959", "Will", "Blue", "Coffee"), ("25.05.1962", "Sheila", "Green", "Tea")]
menuChoice = None

while menuChoice != "0":
    print("\nFamily Members\n")
    print("0 = Exit")
    print("1 = Print Members")
    print("2 = Print example from position 1")
    print("3 = Add An Entry")
 
    menuChoice = input("\nWhat do you want to do? ")

    # Exit
    if menuChoice == "0":
        print("\nThanks for joining!")

    # Print Members
    elif menuChoice == "1":
        print("\nFamily Members\n")
        print("NAME\tBIRTHDAY\tCOLOUR\tHOT DRINKS\n")

        for entry in family:
            bday, name, colour, tea_coffee = entry
            print(name, "\t", bday, "\t", colour, "\t", tea_coffee)

    # Print An Entry
    elif menuChoice == "2":
        print(family[1])  # Print the entry at position 1

    # Add An Entry
    elif menuChoice == "3":
        name = input("\nWhat is the entry's name? ")
        bday = input("\nWhen is their birthday? ")
        colour = input("\nWhat is their favourite colour? ")
        tea_coffee = input("\nDo they prefer tea or coffee? ")

        entry = (bday, name, colour, tea_coffee)
        family.append(entry)
        family.sort(reverse=True)
