from PyQt5 import QtWidgets, QtCore
from base import *

class Params(object):
    def return_key(self):
        with db_session:
            self.c = self.box_select.currentText().split(' ')
            self.key_name = Employee.get(surname=self.c[0], name=self.c[1], patronymic=self.c[2], birthdate=self.c[3]).key
        return self.key_name
    def box(self):
        with db_session:
            self.b = []
            for i in select(c for c in Employee):
                self.b.append('{} {} {} {}'.format(i.surname,i.name,i.patronymic,i.birthdate))
        return self.b
    def findchange(self):
        if self.box_select.currentText() != '':
            with db_session:
                self.label_surname_ident.setText(Employee.get(key=self.return_key()).surname)
                self.label_name_ident.setText(Employee.get(key=self.return_key()).name)
                self.label_patronymic_ident.setText(Employee.get(key=self.return_key()).patronymic)
                self.label_age_ident.setText(str(int((date.today()-Employee.get(key=self.return_key()).birthdate).days//365.25)))
                self.label_post_ident.setText(Employee.get(key=self.return_key()).post)


def test_for_empty(func):
    def wrapper(self):
        with db_session:
            if count(c for c in Employee) == 0:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('В базе нет ни одного сотрудника. Внесите данные.')
                msg.setWindowTitle('Сообщение')
                msg.exec_()
            else:
                func(self)
    return wrapper


def warning(self):
    return self.line_surname.text() == '' or self.line_name.text() == '' or self.line_patronymic.text() == '' or self.line_post.text() == '' or self.line_department.text() == '' or len(self.line_phone.text()) < 14


def message_warning(self, message):
    self.msg = QtWidgets.QMessageBox()
    self.msg.setIcon(QtWidgets.QMessageBox.Warning)
    self.msg.setText(message)
    self.msg.setWindowTitle('Ошибка')
    self.msg.exec_()

def message_info(self, message):
    self.msg = QtWidgets.QMessageBox()
    self.msg.setIcon(QtWidgets.QMessageBox.Information)
    self.msg.setText(message)
    self.msg.setWindowTitle('Информация')
    self.msg.exec_()