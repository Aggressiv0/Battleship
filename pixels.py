import pygame
import font as ft
import window_file as winfile


class Pixel:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.is_there_ship = False

    def display_pixel(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def put_ship(self, mouse):
        # print('mouseDown')
        # print(mouse)
        if (mouse[0] in range(int(self.x), int(self.x) + self.width)
                and mouse[1] in range(int(self.y), int(self.y) + self.height)):
            if not self.is_there_ship:
                # print(list_of_pixels[0].is_there_ship)
                # print(list_of_pixels.index(self))
                # pos_of_pixel = list_of_pixels.index(self)
                self.color = (180, 180, 180)
                self.is_there_ship = True
            else:
                self.color = (255, 255, 255)
                self.is_there_ship = False


list_of_pixels = []

start_x = 0
start_y = 30

for i in range(100):
    if i % 10 == 0:
        start_y += 31
        start_x = 0
    start_x += 31
    pixel = Pixel(start_x, start_y, 30, 30, (255, 255, 255))
    list_of_pixels.append(pixel)
