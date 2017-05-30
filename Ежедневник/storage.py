import sqlite3
import os.path as Path


SQL_ADD_TASK_NAME = '''
INSERT INTO planner (task_name, task_description, task_date) 
VALUES (?,?,?)
'''

SQL_UPD_TASK = '''
UPDATE planner
SET task_name = ?, task_description = ?, task_date = ?
WHERE id = ?
'''



SQL_SELECT_ALL = '''
SELECT id, task_name, task_description, task_date, task_status from planner
'''

def connect(db_name=None):
    if db_name is None:
        db_name = 'base.db'

    conn = sqlite3.connect(db_name)

    return conn


def initialize(conn):
    with conn:
        script_file_path = Path.join(Path.dirname(__file__), 'schema.sql')

        with open(script_file_path) as f:
            conn.executescript(f.read())


def add_upd_task(conn):
    with conn:
        task_id_upd = input('Введите номер редактируемой задачи: ')
        task_upd = input('Введите новое название задачи: ')
        task_desk_upd = input('Введите новое описание задачи: ')
        task_da_upd = input('Введите новую дату задачи: ')
        conn.execute(SQL_UPD_TASK,[task_upd, task_desk_upd, task_da_upd, task_id_upd])
    return


def add_task_name(conn):
    with conn:
        task = input('Введите название задачи: ')
        task_desk = input('Введите описание задачи: ')
        task_da = input('Введите дату задачи: ')
        conn.execute(SQL_ADD_TASK_NAME,[task, task_desk, task_da])
    return

def find_all(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()
