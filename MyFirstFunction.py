def happyBirthday():
    """Print 'Happy Birthday!'"""
    print("Happy Birthday!")

def notYourBirthday():
    """Print 'It's not your birthday, but have a good day!'"""
    print("It's not your birthday, but have a good day!")

# Ask the user if it's their birthday
user_input = input("Is it your birthday today? (Y/N): ")

# Check the user input and call the appropriate function
if user_input.lower() == 'y':
    happyBirthday()
else:
    notYourBirthday()
