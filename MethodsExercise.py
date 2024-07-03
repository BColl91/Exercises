#Create a new Computer class which will include the totalDevices class attribute, initially set to zero;
class Computer:
	totalDevices = 0 
#Create a constructor method which will receive model and type parameters when an object is created and print "A new VAIO laptop has been manufactured.", where VAIO is the model and laptop is the type passed when a Computer object has been substantiated;
	def __init__(self, model, type):
		self.model = model
		self.type = type
		Computer.totalDevices += 1
		print("A new {} {} has been manufactured.".format(self.model, self.type))
#Create a static method called displayTotal(), which will print "The total number of units produced is", followed by the totalDevices class attribute; 
	def displayTotal():
		print("The total number of units produced is", Computer.totalDevices)

#Create four new objects of your choice, perhaps called sony, dell, hp, and asus, passing appropriate model and type parameters;
sony = Computer("VAIO", "laptop")
dell = Computer("Inspiron", "desktop")
hp = Computer("Pavilion", "Tablet")
asus = Computer("ZenBook", "laptop")

#Invoke the static method after the objects have been created.
Computer.displayTotal()

