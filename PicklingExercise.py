import pickle
import shelve


#List of Food
food_list = ["apple", "banana", "carrot", "doughnut", "eggplant"]

#Pickle the list
file = open("food_list.dat", "wb")
pickle.dump(food_list, file)
file.close()

file = open("food_list.dat", "rb")
loaded_food_list = pickle.load(file)
file.close()
print("Un-pickled food list:", loaded_food_list)

#shelf files
shelf = shelve.open("my_shelf.db", "c")
shelf["Games"] = ["Final Fantasy", "Crab Game", "Baldurs Gate 3"]
shelf["Hobbies"] = ["reading", "painting", "gardening"]
shelf["Movies"] = ["Inception", "The Matrix", "Resident Evil"]
shelf.sync()
shelf.close()

#read-only mode, un-pickle and print
shelf = shelve.open("my_shelf.db", "r")
print("\nRetrieving un-pickled list")
print("\nGames: ", shelf["Games"])
print("\nHobbies: ", shelf["Hobbies"])
print("\nMovies: ", shelf["Movies"])
shelf.close()
