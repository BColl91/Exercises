from livewires import games
games.init(screen_width=640, screen_height=480, fps=50)
sky = games.load_image("Background.jpg", transparent=False)
games.screen.background = sky
games.screen.mainloop()