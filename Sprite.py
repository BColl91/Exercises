from livewires import games, color
games.init(screen_width=640, screen_height=480, fps=50)
sky = games.load_image("Background.jpg", transparent=False)
games.screen.background = sky
Star_image = games.load_image("Star.png")
Star = games.Sprite(image=Star_image, x=320, y=20)  
games.screen.add(Star)
Title = games.Text(value="Sprite Exercise", size=50, color=color.blue, x=320, y=30)
games.screen.add(Title)

over_message = games.Message(value="Game Over!", 
							size=50, color=color.red,
							x=games.screen.width / 2,
							y=games.screen.height / 2,
							lifetime=500,
							after_death=games.screen.quit)
games.screen.add(over_message)

games.screen.mainloop()
