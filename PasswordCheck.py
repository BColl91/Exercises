#Password

userName = input("Please enter your user name: ")
while userName == "":
 userName = input("Please enter your user name: ")

 
if userName == "User1":
 adminUser = True
else:
 adminUser = False
 
if userName == "User2":
 normalUser = True
else:
 normalUser = False
print("")
if adminUser or normalUser == False:
 print("Invalid User")
userName = input("Please enter your user name: ")
print("")
if adminUser or normalUser == True:
 password = input("Please Enter Your Password: ")
print("")
while password == "":
 password = input("Please Enter Your Password: ")
if password == "Admin":
 password = True
else:
 password = False
print("")
if normalUser and password == True:
 print("Password Accepted.")
if adminUser and password == True:
 print("Password Accepted; You have administrator privileges.")
if password == False:
 print("Invalid Password.")