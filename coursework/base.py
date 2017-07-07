from datetime import date
from pony.orm import Database, Required, Optional, sql_debug, db_session, select, delete, PrimaryKey, count, avg


db = Database()

class Employee(db.Entity):
    key = PrimaryKey(int, auto=True)
    surname = Required(str) #фамилия
    name = Required(str) #имя
    patronymic = Required(str) #отчество
    birthdate = Optional(date) #дата рождения
    sex = Optional(str) #пол
    phone = Optional(str) #телефон
    email = Optional(str) #почта
    post = Optional(str) #должность
    department = Optional(str) #отдел
    date_of_recruitment = Optional(date) #дата приема на работу
    marital_status = Optional(str) #семейное положение
    date_start_vacation = Optional(date) #дата начала отпуска
    date_finish_vacation = Optional(date) #дата окончания отпуска
    kind_vacation = Optional(str) #вид отпуска
    balance = Optional(float) #техническое поле для рассчета даты дня рождения

sql_debug(True)
db.bind('sqlite', 'employee.sqlite', create_db=True)
db.generate_mapping(create_tables=True)