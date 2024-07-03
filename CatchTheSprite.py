from livewires import games, color
import random

games.init(screen_width=640, screen_height=440, fps=50)

class Net(games.Sprite):
	image=games.load_image("Bunny.png")
	
	def __init__(self):
		super(Net, self).__init__(	image=Net.image,
									x=games.mouse.x,
									bottom=games.screen.height)
		self.score=games.Text(	value=0, size=50, color=color.white,
								top=5, right=games.screen.width - 10)
		self.score.value += 10
		games.screen.add(self.score)
	
	def update(self):
		self.x = games.mouse.x
		if self.left < 0:
			self.left = 0
		if self.right > games.screen.width:
			self.right = games.screen.width
		self.check_catch()
			
	def check_catch(self):
		for star in self.overlapping_sprites:
			self.score.value += 10
			self.score.right = games.screen.width - 10
			star.handle_caught()
			
class star(games.Sprite):
	image=games.load_image("star.png")
	speed=3
	
	def __init__(self, x, y=70):
		super(star, self).__init__(image=star.image,
										x=x, y=y,
										dy=star.speed)

	def update(self):
		if self.bottom > games.screen.height:
			self.end_game()
			self.destroy()

	def handle_caught(self):
		self.destroy()
	
	def end_game(self):
		end_message=games.Message(	value="Game Over!", size=90,
									color=color.yellow,
									x=games.screen.width/2,
									y=games.screen.height/2,
									lifetime= 5 * games.screen.fps,
									after_death = games.screen.quit)
		games.screen.add(end_message)
		
class Moon(games.Sprite):
	image=games.load_image("moon.png")
	
	def __init__(self, y=20, speed=3, odds_change=200):
		super(Moon, self).__init__(	image=Moon.image,
											x=games.screen.width/2,
											y=y, dx=speed)
		self.odds_change = odds_change
		self.time_til_drop = 0
	
	def update(self):
		if self.left < 0 or self.right > games.screen.width:
			self.dx = -self.dx
		elif random.randrange(self.odds_change) == 0:
			self.dx = -self.dx
		self.check_drop()
		
	def check_drop(self):
		if self.time_til_drop > 0:
			self.time_til_drop -= 1
		else:
			new_star = star(x=self.x)
			games.screen.add(new_star)
			self.time_til_drop = int(new_star.height * 1.2 / star.speed) + 1
		
def main():
	sky = games.load_image("Background.jpg", transparent=False)
	games.screen.background = sky

	the_moon = Moon()
	games.screen.add(the_moon)
	
	the_net = Net()
	games.screen.add(the_net)

	games.mouse.is_visible = False
	games.screen.event_grab = True
	
	games.screen.mainloop()

main()