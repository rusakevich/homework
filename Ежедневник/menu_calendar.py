from storage import *

def menu_1():
    print('Список задач\n')
    print(find_all(connect()))
def menu_2():
    print ('Добавьте задачу\n')
    add_task_name(connect())
def menu_3():
    print ('Отредактируйте задачу\n')
    add_upd_task(connect())
def menu_4():
    print ('Завершите задачу\n')
def menu_5():
    print ('Начните задачу сначала\n')
def menu_6():
    print ('Выход')

menu_all = {1:menu_1, 2:menu_2, 3:menu_3, 4:menu_4, 5:menu_5, 6:menu_6}