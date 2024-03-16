import pygame
import window_file as winfile
import pixels as px
import start_button as stbtt
import alert_file

mouse_structure = 0

alert = False
set_start_time = False
start_time = 0
run = True

while run:
    winfile.window.fill([0, 0, 0])
    bad_ship_pos = 0
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        mouse_structure = stbtt.StartButton1.cover_button(mouse)
        mouse_structure += stbtt.StartButton2.cover_button(mouse)

        if mouse_structure > 0:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if event.type == pygame.MOUSEBUTTONDOWN:
            alert, set_start_time = stbtt.StartButton1.click_button(mouse, alert, set_start_time,
                                                                    px.player_one)
            alert, set_start_time = stbtt.StartButton2.click_button(mouse, alert, set_start_time,
                                                                    px.player_two)

            #px.player_one.list_of_pixels

            for i in px.player_one.list_of_pixels:
                px.Pixel.put_ship(i, mouse)
            for i in px.player_two.list_of_pixels:
                px.Pixel.put_ship(i, mouse)

    # print(alert, 'x')
    if alert:
        alert, set_start_time, start_time = alert_file.alertf(alert, set_start_time, start_time)

    for i in px.player_one.list_of_pixels:
        px.Pixel.display_pixel(i, winfile.window)

    for i in px.player_two.list_of_pixels:
        px.Pixel.display_pixel(i, winfile.window)

    stbtt.StartButton1.draw_button(winfile.window)
    stbtt.StartButton2.draw_button(winfile.window)

    pygame.display.update()
