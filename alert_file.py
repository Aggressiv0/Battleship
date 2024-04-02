import window_file as winfile
import time
import font as ft


def alertf(alert, set_start_time, start_time):
    if set_start_time:
        start_time = round(time.time() * 1000)
        set_start_time = False
    text = ft.font.render('YOU CANT DO THAT!', False, (255, 255, 255))
    winfile.window.blit(text, (60, 10))
    if start_time + 800 < round(time.time() * 1000):
        print('Koniec czasu')
        start_time = 0
        alert = False
    # print(start_time, round(time.time() * 1000))
    return alert, set_start_time, start_time
