import pygame
import font as ft
import ships_file as shipfl
import test


class Button:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_button(self, window):
        background = pygame.draw.rect(window, self.color, self.rect)
        text = ft.font.render('Potwierdź', True, 'black')
        window.blit(text, background)

    def cover_button(self, mouse):
        if self.rect.collidepoint(mouse):
            self.color = 'gray'
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            self.color = 'white'
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def click_button(self, mouse):
        if self.rect.collidepoint(mouse):
            print('Przycisk potwierdź')
            shipfl.create_ships()
            test.testy()


StartButton = Button(120, 400, 110, 35, 'white')
