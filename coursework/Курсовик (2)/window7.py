from PyQt5 import QtWidgets, QtCore
from base import *


class Window7(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.tunning()
    def tunning(self):
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle('Общая статистика')
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(1)
        self.table.setRowCount(9) 
        self.table.setVerticalHeaderLabels(['Количество сотрудников', 'Количество мужчин','Количество женщин', 'Средний возраст', 'Средний возраст мужчин', 'Средний возраст женщин', 'Среднее время работы', 'Среднее время работы мужчин', 'Среднее время работы женщин'])
        self.table.setHorizontalHeaderLabels(['Значение'])
        with db_session:
            self.count_all = count(c for c in Employee)
            self.count_man = count(c for c in Employee if c.sex == 'Мужской')
            self.count_woman = count(c for c in Employee if c.sex == 'Женский')
            self.table.setItem(0, 0, QtWidgets.QTableWidgetItem(str(self.count_all)))
            self.table.setItem(1, 0, QtWidgets.QTableWidgetItem(str(self.count_man)))
            self.table.setItem(2, 0, QtWidgets.QTableWidgetItem(str(self.count_woman)))
            self.worker = select(c for c in Employee)
            self.worker_man = select(c for c in Employee if c.sex == 'Мужской' )
            self.worker_woman = select(c for c in Employee if c.sex == 'Женский')
            self.years_age = 0
            self.years_age_man = 0
            self.years_age_woman = 0
            self.years_recruitment = 0
            self.years_recruitment_man = 0
            self.years_recruitment_woman = 0
            for i in self.worker:
                self.years_age += (date.today()-i.birthdate).days/365.25
                self.years_recruitment += (date.today()-i.date_of_recruitment).days/365.25
            for i in self.worker_man:
                self.years_age_man += (date.today()-i.birthdate).days/365.25
                self.years_recruitment_man += (date.today()-i.date_of_recruitment).days/365.25
            for i in self.worker_woman:
                self.years_age_woman += (date.today()-i.birthdate).days/365.25
                self.years_recruitment_woman += (date.today()-i.date_of_recruitment).days/365.25
            self.table.setItem(3, 0, QtWidgets.QTableWidgetItem(str(round(self.years_age/self.count_all,1))))
            self.table.setItem(4, 0, QtWidgets.QTableWidgetItem(str(0 if self.count_man == 0 else round(self.years_age_man/self.count_man,1))))
            self.table.setItem(5, 0, QtWidgets.QTableWidgetItem(str(0 if self.count_woman == 0 else round(self.years_age_woman/self.count_woman,1))))
            self.table.setItem(6, 0, QtWidgets.QTableWidgetItem(str(round(self.years_recruitment/self.count_all,1))))
            self.table.setItem(7, 0, QtWidgets.QTableWidgetItem(str(0 if self.count_man == 0 else round(self.years_recruitment_man/self.count_man,1))))
            self.table.setItem(8, 0, QtWidgets.QTableWidgetItem(str(0 if self.count_woman == 0 else round(self.years_recruitment_woman/self.count_woman,1))))
        self.table.resizeColumnsToContents()
        self.gbox = QtWidgets.QGridLayout()
        self.gbox.addWidget(self.table,0,0)
        self.setLayout(self.gbox)


