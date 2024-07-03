class Van(object):
	def __init__(self, model, colour):
		self.model = model
		self.colour = colour
		if self.model == "Transit" and self.colour == "red":
			print("A new red Transit has come off the production line.")
	def __str__(self):
		return "Model: {}, Colour: {}".format(self.model, self.colour)

Ford = Van("Transit", "red")
Volkswagen = Van("Transporter", "blue")

print("\nVan Details:")
print("Ford- ", Ford)
print("Volkswagen- ", Volkswagen)

print("\nAccessing attributes directly:")
print("Ford Model: ")
print(Ford.model)
print("Ford Colour: ")
print(Ford.colour)
print("Volkswagen Model:")
print(Volkswagen.model)
print("Volkswagen Colour: ")
print(Volkswagen.colour)