from livewires import games, color
games.init(screen_width=640, screen_height=480, fps=50)
class Star(games.Sprite):
    def update(self):
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy
def main():
    sky = games.load_image("Background.jpg", transparent=False)
    games.screen.background = sky

    star_image = games.load_image("star.png")
    the_star = Star(image=star_image, x=50, y=50, dx=3, dy=3)
    games.screen.add(the_star)

    games.screen.mainloop()

main()
