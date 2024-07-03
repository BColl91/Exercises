# Ask the user to enter a decimal number. Use try/Except
error = False

try:
    decimal_input = input("Please enter a decimal number: ")
    decimal_number = float(decimal_input)

except ValueError:
    print("Error: Invalid input. Please enter a valid decimal number.")
    print("Python Error Message:", ValueError)
    error = True

if not error:
    print("Valid decimal number entered:", decimal_number)
print(""" """)

# Ask the user to enter the current hour.
try:
    hour_input = input("Please enter the current hour (0-24): ")
    hour = int(hour_input)
    if hour < 0 or hour > 24:
         print("Invalid hour")
except ValueError:
    if str(ValueError) == "Invalid hour":
        print("Error: The hour entered is not in the range 0 to 24.")
    else:
        print("Error: Not a number. Please enter a valid hour.")
    print("Python Error Message:", ValueError)
    error = True
	
if error == False:
    print("Valid hour entered:", hour)
