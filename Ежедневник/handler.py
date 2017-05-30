from menu_calendar import *
from storage import *
def menu_handler():
    paragraph = 1
    while int(paragraph) != max(menu_all):
        paragraph = input('Введите число: ')
        if paragraph.isdigit() and int(paragraph) != 0:
            menu_all.get(int(paragraph))() if int(paragraph) in menu_all.keys() else print('Такого пункта меню ещё нет!!!\n')
        else:
            print('Ошибка!!! Введены некорректные данные!!!\n')
            paragraph = 1


print('Ежедневник. Выберите действие:\n')
print('1. Вывести список задач')
print('2. Добавить задачу')
print('3. Отредактировать задачу')
print('4. Завершить задачу')
print('5. Начать задачу сначала')
print('6. Выход\n')

connect()
initialize(connect())

menu_handler()
