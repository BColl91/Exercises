from livewires import games, color
import random
games.init(screen_width=640, screen_height=440, fps=50)
class Net(games.Sprite):
	def update(self):
		self.x = games.mouse.x
		self.y = games.mouse.y
		self.check_collide()

	def check_collide(self):
		for strs in self.overlapping_sprites:
			strs.handle_collide()
			
class Star(games.Sprite):
	def handle_collide(self):
		self.x = random.randrange(games.screen.width)
		self.y = random.randrange(games.screen.height)
		
def main():
	sky = games.load_image("Background.jpg", transparent=False)
	games.screen.background = sky

	star_image = games.load_image("star.png")
	star_x = random.randrange(games.screen.width)
	star_y = random.randrange(games.screen.height)
	stars = Star(image=star_image, x=star_x, y=star_y)
	games.screen.add(stars)

	Rabbit = games.load_image("Bunny.png")
	Bunn = Net(image=Rabbit, x=games.mouse.x, y=games.mouse.y)
	games.screen.add(Bunn)
	games.mouse.is_visible = False
	games.screen.event_grab = True
	
	user_message = games.Message(value="Try to catch the stars!", 
							size=50, color=color.yellow,
							x=games.screen.width/2,
							y=games.screen.height/2,
							lifetime=100)
	games.screen.add(user_message)

	games.screen.mainloop()

main()
