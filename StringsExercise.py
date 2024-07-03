# Concatenation example
#Baa baa black sheep
line1 = "\nBaa baa black sheep, have you any wool?\n"
line2 = "\nYes sir, yes sir, three bags full!\n"
join1 = line1 + line2
line3 = "\nOne for the master, one for the dame,\n"
line4 = "\nAnd one for the little boy who lives down the lane.\n"
join2 = line3 + line4
nurseryRhyme = join1 + join2
print(nurseryRhyme)
print("")
# String slice examples

print(line3)
print("")
print(nurseryRhyme[76:115])
print("")
# Membership operators examples (in)
checkIn = "the" in line3
print(checkIn)
print("")
# Checking string attributes
print("Try it now")
trytitle = "Try it now"
title = trytitle.istitle()
print(title)
print("")
print("TRY IT NOW")
trycaps = "TRY IT NOW"
lower = trycaps.islower()
print(lower)
upper = trycaps.isupper()
print(upper)