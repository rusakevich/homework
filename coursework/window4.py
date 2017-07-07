from PyQt5 import QtWidgets, QtCore
from base import *


class Window4(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.tunning()
    def tunning(self):
        self.setGeometry(300, 300, 1000, 300)
        self.setWindowTitle('Данные всех сотрудников')
        with db_session:
            self.worker = count(c for c in Employee)
        self.table = QtWidgets.QTableWidget()         
        self.table.setColumnCount(7)
        self.table.setRowCount(self.worker)  
        self.table.setHorizontalHeaderLabels(['ФИО', 'Должность','Отдел', 'Телефон', 'Почта','Отпуск', 'Кол-во дней в компании'])
        with db_session:
            self.keys = select(c.key for c in Employee)
            for i in range(self.worker):
                self.table.setItem(i, 0, QtWidgets.QTableWidgetItem('{} {} {}'.format(Employee.get(key=list(self.keys)[i]).surname, Employee.get(key=list(self.keys)[i]).name, Employee.get(key=list(self.keys)[i]).patronymic)))
                self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(Employee.get(key=list(self.keys)[i]).post))
                self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(Employee.get(key=list(self.keys)[i]).department))
                self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(Employee.get(key=list(self.keys)[i]).phone))
                self.table.setItem(i, 4, QtWidgets.QTableWidgetItem(Employee.get(key=list(self.keys)[i]).email))
                if Employee.get(key=list(self.keys)[i]).date_start_vacation is None or Employee.get(key=list(self.keys)[i]).date_finish_vacation is None:
                    self.vac = 'на работе'
                else:
                    self.vac = 'в отпуске' if date.today() >= Employee.get(key=list(self.keys)[i]).date_start_vacation and date.today() <= Employee.get(key=list(self.keys)[i]).date_finish_vacation else 'на работе'
                self.table.setItem(i, 5, QtWidgets.QTableWidgetItem(self.vac))
                self.table.setItem(i, 6, QtWidgets.QTableWidgetItem(str((date.today()-Employee.get(key=list(self.keys)[i]).date_of_recruitment).days)))
        self.table.sortByColumn(0,0)
        self.table.resizeColumnsToContents()
        self.gbox = QtWidgets.QGridLayout()
        self.gbox.addWidget(self.table,0,0)
        self.setLayout(self.gbox)