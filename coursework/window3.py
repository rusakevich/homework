from PyQt5 import QtWidgets, QtCore
from base import *
from __init__ import Params, message_info


class Window3(QtWidgets.QWidget, Params):
    def __init__(self,parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.tunning()
    def tunning(self):
        self.setWindowTitle('Удалить данные сотрудника')
        self.spacer1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.spacer2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.spacer3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.spacer4 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.label_select = QtWidgets.QLabel('Сотрудник')
        self.label_surname = QtWidgets.QLabel('Фамилия')
        self.label_name = QtWidgets.QLabel('Имя')
        self.label_patronymic = QtWidgets.QLabel('Отчество')
        self.label_age = QtWidgets.QLabel('Возраст')
        self.label_post = QtWidgets.QLabel('Должность')
        self.label_surname_ident = QtWidgets.QLabel()
        self.label_surname_ident.setStyleSheet('font-size: 12pt')
        self.label_name_ident = QtWidgets.QLabel()
        self.label_name_ident.setStyleSheet('font-size: 12pt')
        self.label_patronymic_ident = QtWidgets.QLabel()
        self.label_patronymic_ident.setStyleSheet('font-size: 12pt')
        self.label_age_ident = QtWidgets.QLabel()
        self.label_age_ident.setStyleSheet('font-size: 12pt')
        self.label_post_ident = QtWidgets.QLabel()
        self.label_post_ident.setStyleSheet('font-size: 12pt')
        self.box_select = QtWidgets.QComboBox()                  
        self.box_select.addItems(self.box())
        self.box_select.setToolTip('Выберите сотрудника')
        self.btnExit = QtWidgets.QPushButton('Закрыть')
        self.btnDel = QtWidgets.QPushButton('Удалить')
        self.btnDelExit = QtWidgets.QPushButton('Удалить и закрыть')
        self.btnExit.setToolTip('Закрыть')
        self.btnDelExit.setToolTip('Удалить данные сотрудника и закрыть')
        self.btnDel.setToolTip('Удалить данные сотрудника')
        self.gbox = QtWidgets.QGridLayout(self)
        self.gbox.addItem(self.spacer1,0,0,1,2)
        self.gbox.addItem(self.spacer3,1,0,7,1)
        self.gbox.addWidget(self.label_select,1,1)
        self.gbox.addWidget(self.label_surname,2,1)
        self.gbox.addWidget(self.label_name,3,1)
        self.gbox.addWidget(self.label_patronymic,4,1)
        self.gbox.addWidget(self.label_age,5,1)
        self.gbox.addWidget(self.label_post,6,1)
        self.gbox.addWidget(self.box_select,1,2)
        self.gbox.addWidget(self.label_surname_ident,2,2)
        self.gbox.addWidget(self.label_name_ident,3,2)
        self.gbox.addWidget(self.label_patronymic_ident,4,2)
        self.gbox.addWidget(self.label_age_ident,5,2)
        self.gbox.addWidget(self.label_post_ident,6,2)
        self.gbox.addWidget(self.btnDel,7,1,1,2)
        self.gbox.addWidget(self.btnDelExit,8,1)
        self.gbox.addWidget(self.btnExit,8,2)   
        self.gbox.addItem(self.spacer4,1,3,7,1)
        self.gbox.addItem(self.spacer1,9,0,1,2)
        self.findchange()
        self.box_select.currentTextChanged.connect(self.findchange)
        self.btnDelExit.clicked.connect(self.deletexit)
        self.btnDel.clicked.connect(self.deletall)
        self.btnExit.clicked.connect(self.close)
    def delet(self):
        with db_session:
            delete(c for c in Employee if c.key == self.return_key())
        message_info(self, 'Данные сотрудника удалены')
        with db_session:
            if count(c for c in Employee) == 0:
                self.close()
        self.box_select.clear()
        self.box_select.addItems(self.box())
    def deletexit(self):
        self.deletall()
        if self.msg == QtWidgets.QMessageBox.Yes:
            self.close()  
    def deletall(self):
        self.msg = QtWidgets.QMessageBox.question(self, 'Подтверждение', "Действительно хотите удалить данные сотрудника?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if self.msg == QtWidgets.QMessageBox.Yes:
            self.delet()
