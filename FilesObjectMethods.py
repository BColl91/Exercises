# Create your own text file containing the text of your choice

file = open("OscarWilde.txt", "r")
for line in file:
     print(line, end="")
print()
file.close()

print("Reading file line by line:")
file = open("OscarWilde.txt", "w")
poem = "For more poems to lift you up from this dreary world,\n"
poem += "I recommend a book by Quercus called 'Poems for a world gone to sh*t'.\n"
file.write(poem)
file.close()

file = open("OscarWilde.txt", "r")
for line in file:
     print(line, end="")
print()
file.close()

# Open a new text file in "write" mode; create a block of text and write it to the new file
file = open("thePig.txt", "w")
newLine = ("It was an evening in November.\n")
newLine +=("As I very well remember,\n")
newLine +=("I was strolling down the street in drunken pride,\n")
newLine +=("But my knees were all a-flutter,\n")
newLine +=("And I landed in the gutter\n")
newLine +=("And a pig came up and lay down by my side.\n")
newLine +=("Yes, I lay there in the gutter\n")
newLine +=("Thinking thoughts I could not utter,\n")
newLine +=("When a colleen passing by did softly say\n")
newLine +=("'You can tell a man who boozes\n")
newLine +=("By the company he chooses'-\n")
newLine +=("And the pig got up and walked away.\n")
file.write(newLine)
file.close()

print("\n\nContents of the new file:")
with open("thePig.txt", "r") as new_file:
    for line in new_file:
        print(line, end='')
print()
file.close()
