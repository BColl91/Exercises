#ELIF, ELSE and IF
print("Alcohol Test")
print("")
unit = input("How much alcohol do you drink (in units) within a week?")

unit = float(unit)


if unit == 0:
    print("Are you a saint? Or perhaps you are lying")

elif unit <= 10:
    print("You are a moderate drinker. Pat yourself on the back.")

elif unit <= 20:
    print("You are a heavy drinker and borderline alcoholic!")
 
elif unit > 20:
    print("You are a lush! You desperately need to join Alcoholics Anonymous!")