from menu_calendar import *
from storage import *

def menu_handler():
    paragraph = 1
    menu_start()
    while int(paragraph) != max(menu_all):
        
        paragraph = input('Введите число: \n')
        if paragraph.isdigit() and int(paragraph) != 0:
            menu_all.get(int(paragraph))() if int(paragraph) in menu_all.keys() else print('Такого пункта меню ещё нет!!!\n')
        else:
            print('Ошибка!!! Введены некорректные данные!!!\n')
            paragraph = 1
            #menu_start()


connect()
initialize(connect())
menu_handler()