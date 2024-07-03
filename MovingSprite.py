from livewires import games
games.init(screen_width=640, screen_height=440, fps=50)
class Net(games.Sprite):

	def update(self):

		self.x = games.mouse.x
		self.y = games.mouse.y
def main():
	sky = games.load_image("Background.jpg", transparent=False)
	games.screen.background = sky
	Rabbit = games.load_image("Bunny.png")
	Bunn = Net(image=Rabbit, x=games.mouse.x, y=games.mouse.y)
	games.screen.add(Bunn)
	games.mouse.is_visible = False
	games.screen.event_grab = True
	games.screen.mainloop()

main()