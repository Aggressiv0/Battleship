import pygame
import window_file as winfile
import pixels as px
import start_button as stbtt
import alert_file

alert = False
set_start_time = False
start_time = 0
run = True

while run:
    winfile.window1.fill([0, 0, 0])
    bad_ship_pos = 0
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        stbtt.StartButton.cover_button(mouse)
        if event.type == pygame.MOUSEBUTTONDOWN:
            alert, set_start_time = stbtt.StartButton.click_button(mouse, alert, set_start_time)
            for i in px.player_one.list_of_pixels:
                px.Pixel.put_ship(i, mouse)
            for i in px.player_two.list_of_pixels:
                px.Pixel.put_ship(i, mouse)
    # print(alert, 'x')
    if alert:
        alert, set_start_time, start_time = alert_file.alertf(alert, set_start_time, start_time)
    for i in px.player_one.list_of_pixels:
        px.Pixel.display_pixel(i, winfile.window1)
    for i in px.player_two.list_of_pixels:
        px.Pixel.display_pixel(i, winfile.window1)
    stbtt.StartButton.draw_button(winfile.window1)
    pygame.display.update()
