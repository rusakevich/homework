from PyQt5 import QtWidgets, QtCore
from base import *


class Window5(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.tunning()
    def tunning(self):
        self.setGeometry(300, 300, 1100, 300)
        self.setWindowTitle('Сотрудники находящиеся в отпуске')
        with db_session:
            self.worker = count(c for c in Employee if date.today() >= c.date_start_vacation and date.today() <= c.date_finish_vacation)
        self.table = QtWidgets.QTableWidget()         
        self.table.setColumnCount(6)
        self.table.setRowCount(self.worker)  
        self.table.setHorizontalHeaderLabels(['ФИО', 'Должность', 'Телефон', 'Даты отпуска','Дней до конца отпуска', 'Вид отпуска'])
        with db_session:
            self.keys = select(c.key for c in Employee if date.today() >= c.date_start_vacation and date.today() <= c.date_finish_vacation)
            for i in range(self.worker):
                self.table.setItem(i, 0, QtWidgets.QTableWidgetItem('{} {} {}'.format(Employee.get(key=list(self.keys)[i]).surname, Employee.get(key=list(self.keys)[i]).name, Employee.get(key=list(self.keys)[i]).patronymic)))
                self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(Employee.get(key=list(self.keys)[i]).post))
                self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(Employee.get(key=list(self.keys)[i]).phone))
                self.table.setItem(i, 3, QtWidgets.QTableWidgetItem('{} - {}'.format(Employee.get(key=list(self.keys)[i]).date_start_vacation, Employee.get(key=list(self.keys)[i]).date_finish_vacation)))
                self.table.setItem(i, 4, QtWidgets.QTableWidgetItem(str((Employee.get(key=list(self.keys)[i]).date_finish_vacation - date.today()).days)))
                self.table.setItem(i, 5, QtWidgets.QTableWidgetItem(Employee.get(key=list(self.keys)[i]).kind_vacation))
        self.table.sortByColumn(0,0)
        self.table.resizeColumnsToContents()
        self.gbox = QtWidgets.QGridLayout()
        self.gbox.addWidget(self.table,0,0)
        self.setLayout(self.gbox)