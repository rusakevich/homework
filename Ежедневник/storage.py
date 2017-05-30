import sqlite3
import os.path as Path
from datetime import date
import calendar

######################
SQL_SELECT_ALL = '''
SELECT id, task_name, task_description, task_date, task_status FROM planner
'''

SQL_SELECT = '''
SELECT id, task_name, task_description, task_date, task_status FROM planner WHERE task_date = ?
'''

SQL_ADD_TASK_NAME = '''
INSERT INTO planner (task_name, task_description, task_date) 
VALUES (?,?,?)
'''

SQL_UPD_TASK = '''
UPDATE planner
SET task_name = ?, task_description = ?, task_date = ?
WHERE id = ?
'''

SQL_UPD_END = '''
UPDATE planner
SET task_status = 'Выполнено'
WHERE id = ?
'''

SQL_UPD_BEGIN = '''
UPDATE planner
SET task_status = 'Не выполнено'
WHERE id = ?
'''

SQL_DEL_ALL = '''DELETE FROM planner'''

SQL_SELECT_ID = '''SELECT id FROM planner WHERE id>0'''

######################
######################
def connect(db_name=None):
    '''создание соединения'''
    if db_name is None:
        db_name = 'base.db'
    conn = sqlite3.connect(db_name)
    return conn

######################
def initialize(conn):
    '''создание таблицы'''
    with conn:
        script_file_path = Path.join(Path.dirname(__file__), 'schema.sql')
        with open(script_file_path) as f:
            conn.executescript(f.read())
  

 #######################
def sql_select_all(conn):
    '''вывод всего списка задач'''
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        for row in cursor.fetchall():
            for i in row:
                print('|{0:15}|'.format(i), end='')
            print('') 
        print('')


#######################
def sql_select(conn):
    '''вывод списка задач на дату'''
    with conn:
        conf = input('На текущий день y/n? ')
        if conf == 'y' or conf == 'Y':
            dat = date.today()
        else:
            ye = input('Введите год: ')
            while not ye.isdigit() or int(ye) > date.today().year + 100 or int(ye) < date.today().year:
                ye = input('Введите корректный год: ')

            mon = input('Введите месяц: ')
            while not mon.isdigit() or int(mon) > 12 or int(mon) == 0:
                mon = input('Введите корректный месяц: ')
                
            d = input('Введите день: ')
            while not d.isdigit() or int(d) == 0 or int(d) > calendar.monthrange(int(ye), int(mon))[1]:
                d = input('Введите корректный день: ')

            dat = date(int(ye), int(mon), int(d))
        cursor = conn.execute(SQL_SELECT, [dat,])
        for row in cursor.fetchall():
            for i in row:
                print('|{0:15}|'.format(i), end='')
            print('') 
        print('')


########################
def add_task_name(conn):
    '''заведение новой задачи'''
    with conn:
        task = input('Введите название задачи: ')
        task_desk = input('Введите описание задачи: ')

        ye = input('Введите год: ')
        while not ye.isdigit() or int(ye) > date.today().year + 100 or int(ye) < date.today().year:
            ye = input('Введите корректный год: ')

        mon = input('Введите месяц: ')
        while not mon.isdigit() or int(mon) == 0 or date(int(ye), int(mon), calendar.monthrange(int(ye), int(mon))[1]) < date(int(ye), date.today().month, date.today().day):
           mon = input('Введите корректный месяц: ')

        d = input('Введите день: ')
        while not d.isdigit() or int(d) == 0 or int(d) > calendar.monthrange(int(ye), int(mon))[1] or date(int(ye), int(mon), int(d)) < date(date.today().year, date.today().month, date.today().day):
           d = input('Введите корректный день: ')

        task_da = date(int(ye), int(mon), int(d))
        conn.execute(SQL_ADD_TASK_NAME,[task, task_desk, task_da])
    return


#########################
def add_upd_task(conn):
    '''редактирование выбранной задачи'''
    with conn:
        task_id_upd = input('Введите ID редактируемой задачи: ')

        while sql_select_id(connect(), task_id_upd) == 0:
            task_id_upd = input('Такого ID не существует, введите существующий: ')

        task_upd = input('Введите новое название задачи: ')
        task_desk_upd = input('Введите новое описание задачи: ')

        ye = input('Введите год: ')
        while not ye.isdigit() or int(ye) > date.today().year + 100 or int(ye) < date.today().year:
            ye = input('Введите корректный год: ')

        mon = input('Введите месяц: ')
        while not mon.isdigit() or int(mon) == 0 or date(int(ye), int(mon), calendar.monthrange(int(ye), int(mon))[1]) < date(int(ye), date.today().month, date.today().day):
           mon = input('Введите корректный месяц: ')

        d = input('Введите день: ')
        while not d.isdigit() or int(d) == 0 or int(d) > calendar.monthrange(int(ye), int(mon))[1] or date(int(ye), int(mon), int(d)) < date(date.today().year, date.today().month, date.today().day):
           d = input('Введите корректный день: ')

        task_da_upd = date(int(ye), int(mon), int(d))

        conn.execute(SQL_UPD_TASK,[task_upd, task_desk_upd, task_da_upd, task_id_upd])
    return


#########################
def add_upd_end(conn):
    '''завершение выбранной задачи'''
    with conn:
        task_id_end = input('Введите ID завершаемой задачи: ')

        while sql_select_id(connect(), task_id_end) == 0:
            task_id_end = input('Такого ID не существует, введите существующий: ')

        conn.execute(SQL_UPD_END,[task_id_end,])
    return


#########################
def add_upd_begin(conn):
    '''начало задачи заново'''
    with conn:
        task_id_begin = input('Введите ID задачи, которую начнем сначала: ')

        while sql_select_id(connect(), task_id_begin) == 0:
            task_id_begin = input('Такого ID не существует, введите существующий: ')

        conn.execute(SQL_UPD_BEGIN,[task_id_begin,])
    return


#########################
def del_all(conn):
    '''очистка таблицы'''
    with conn:
        conn.execute(SQL_DEL_ALL)
    return

#########################
def sql_select_id(conn, identificator):
    '''определение входит ли id в таблицу'''
    with conn:
        cursor = conn.execute(SQL_SELECT_ID)
    c=[]
    for i in cursor.fetchall():
        c.append(i[0])
    if identificator.isdigit():
        return 1 if int(identificator) in c else 0 
    else:
        return 0
