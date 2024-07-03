phrase = input("\nEnter a word or phrase: ")
for character in phrase:
 print(character)

numChars = len(phrase)
print("You have entered", numChars, "characters")

print("\nCounting in increments of 20, from 20 to 100:")
for n in range(20, 120, 20):
	print(n)
	
#Nested loop (a loop within a loop)
for n in range(3):
 for i in range(5):
  print("The inner loop count =", i)
 print("The outer loop count =", n )
 