import pygame


class Window:
    def __init__(self):
        self.window_width = 800
        self.window_height = 800
        self.window_size = (self.window_width, self.window_height)
        self.icon_img = pygame.image.load('img/ship_icon.jpg')

    def create_widnow(self):
        window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption('Battleship')
        pygame.display.set_icon(self.icon_img)
        return window


win = Window()

window = win.create_widnow()
