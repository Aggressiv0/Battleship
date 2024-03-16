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


# list_of_pixels = []
#
# start_x = 0
# start_y = 30
#
# for i in range(100):
#     if i % 10 == 0:
#         start_y += 31
#         start_x = 0
#     start_x += 31
#     pixel = Pixel(start_x, start_y, 30, 30, (255, 255, 255))
#     list_of_pixels.append(pixel)
#
# start_x1 = 330
# start_y1 = 30
#
# for i in range(100):
#     if i % 10 == 0:
#         start_y1 += 31
#         start_x1 = 330
#     start_x1 += 31
#     pixel = Pixel(start_x1, start_y1, 30, 30, (255, 255, 255))
#     list_of_pixels.append(pixel)


class Player:
    def __init__(self, start_x, start_y):
        self.list_of_pixels = []
        self.list_of_ships = []
        self.start_x = start_x
        self.start_y = start_y

    def create_board(self):
        const_start_x = self.start_x
        for i in range(100):
            if i % 10 == 0:
                self.start_y += 31
                self.start_x = const_start_x
            self.start_x += 31
            pixel = Pixel(self.start_x, self.start_y, 30, 30, (255, 255, 255))
            self.list_of_pixels.append(pixel)


player_one = Player(0, 30)
player_two = Player(330, 30)

player_one.create_board()
player_two.create_board()
