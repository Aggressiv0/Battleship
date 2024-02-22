import pygame
import window_file as winfile
import pixels as px
import start_button as stbtt
import alert_file

run = True

while run:
    winfile.window.fill([0, 0, 0])
    bad_ship_pos = 0
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        stbtt.StartButton.cover_button(mouse)
        if event.type == pygame.MOUSEBUTTONDOWN:
            stbtt.StartButton.click_button(mouse)
            for i in px.list_of_pixels:
                px.Pixel.put_ship(i, mouse)
    for i in px.list_of_pixels:
        px.Pixel.display_pixel(i, winfile.window)
    stbtt.StartButton.draw_button(winfile.window)
    pygame.display.update()
