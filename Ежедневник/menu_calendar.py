from storage import *

def menu_1():
    print('Весь список задач:')
    sql_select_all(connect())
def menu_2():
    print('Список задач на дату')
    sql_select(connect())
def menu_3():
    print('Добавьте задачу')
    add_task_name(connect())
def menu_4():
    print('Отредактируйте задачу')
    add_upd_task(connect())
def menu_5():
    print('Завершите задачу')
    add_upd_end(connect())
def menu_6():
    print('Начните задачу сначала')
    add_upd_begin(connect())
def menu_7():
    print('Все задачи очищены')
    del_all(connect())
def menu_8():
    print('Меню:')
    menu_()
def menu_9():
    print ('Выход')


def menu_start():
    print('Ежедневник. Выберите действие:\n')
    print('1. Вывести весь список задач')
    print('2. Вывести список задач на дату')
    print('3. Добавить задачу')
    print('4. Отредактировать задачу')
    print('5. Завершить задачу')
    print('6. Начать задачу сначала')
    print('7. Очистка всех задач')
    print('8. Вывод меню')
    print('9. Выход\n')

def menu_():
    print('1. Вывести весь список задач')
    print('2. Вывести список задач на дату')
    print('3. Добавить задачу')
    print('4. Отредактировать задачу')
    print('5. Завершить задачу')
    print('6. Начать задачу сначала')
    print('7. Очистка всех задач')
    print('8. Вывод меню')
    print('9. Выход\n')





menu_all = {1:menu_1, 2:menu_2, 3:menu_3, 4:menu_4, 5:menu_5, 6:menu_6, 7:menu_7, 8:menu_8, 9:menu_9}