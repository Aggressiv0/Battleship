import pygame
import pixels as px


class Ship:
    def __init__(self, list_elem_ship, length):
        self.list_elem_ship = list_elem_ship
        self.length = length


list_all_ships = []


def create_ships():
    length = 0
    list_elem_ship = []
    list_all_ships = []
    for x in range(len(px.list_of_pixels)):
        print(px.list_of_pixels[x].is_there_ship)
        if px.list_of_pixels[x].is_there_ship:
            if not px.list_of_pixels[x - 10].is_there_ship:
                if x + 10 > 99:
                    length += 1
                    list_elem_ship.append(x)
                else:
                    if not px.list_of_pixels[x + 10].is_there_ship:
                        length += 1
                        list_elem_ship.append(x)
                    else:
                        print('Błąd')
                        break
            else:
                print('Błąd')
                break
        if ((not px.list_of_pixels[x].is_there_ship
                or (x-9) % 10 == 0
                or x == 99) and length > 0):
            ship = Ship(list_elem_ship, length)
            list_all_ships.append(ship)
            list_elem_ship = []
            length = 0
        if length > 4:
            print('Błąd')
            break
    for i in list_all_ships:
        print(i.list_elem_ship, i.length)
