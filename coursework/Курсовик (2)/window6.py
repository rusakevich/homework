from math import ceil
from PyQt5 import QtWidgets, QtCore
from base import *


class Window6(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.tunning()
    def tunning(self):
        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('Сотрудники с ближайшими днями рождения')
        with db_session:
            self.keys = select(c.key for c in Employee)
            for i in range(count(c for c in Employee)):
                Employee.get(key=list(self.keys)[i]).balance = (date.today()-Employee.get(key=list(self.keys)[i]).birthdate).days%365.25
            self.worker = count(c.key for c in Employee if c.balance > 350)
        self.table = QtWidgets.QTableWidget()           
        self.table.setColumnCount(5)
        self.table.setRowCount(self.worker)  
        self.table.setHorizontalHeaderLabels(['ФИО', 'Должность', 'Отдел', 'День рождения','Дней до дня рождения'])
        with db_session:
            self.keys = select(c.key for c in Employee if c.balance > 350)
            for i in range(self.worker):
                self.table.setItem(i, 0, QtWidgets.QTableWidgetItem('{} {} {}'.format(Employee.get(key=list(self.keys)[i]).surname, Employee.get(key=list(self.keys)[i]).name, Employee.get(key=list(self.keys)[i]).patronymic)))
                self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(Employee.get(key=list(self.keys)[i]).post))
                self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(Employee.get(key=list(self.keys)[i]).department))
                self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(Employee.get(key=list(self.keys)[i]).birthdate)))
                self.table.setItem(i, 4, QtWidgets.QTableWidgetItem(str(ceil(365-Employee.get(key=list(self.keys)[i]).balance))))
        self.table.sortByColumn(0,0)
        self.table.resizeColumnsToContents()
        self.gbox = QtWidgets.QGridLayout()
        self.gbox.addWidget(self.table,0,0)
        self.setLayout(self.gbox)