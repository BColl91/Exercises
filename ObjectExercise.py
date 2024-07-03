# Define the Car class
class Car:
	def fill_up(self):
		print("Insert enough fuel to fill me up.")
    
	def accelerate(self):
		print("Press the accelerator pedal to increase speed.")

# Instantiate two objects based on the Car class
audi = Car()
volvo = Car()

# Access both methods for both instances
print("Audi:")
audi.fill_up()
audi.accelerate()

print("\nVolvo:")
volvo.fill_up()
volvo.accelerate()