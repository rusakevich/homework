from PyQt5 import QtWidgets, QtCore, QtGui
from __init__ import test_for_empty
from window1 import Window1
from window2 import Window2
from window3 import Window3
from window4 import Window4
from window5 import Window5
from window6 import Window6
from window7 import Window7
from window8 import Window8
from window9 import Window9

class Window(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tunning()
    def tunning(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('База сотрудников')
        self.spacer1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.spacer2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.spacer3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.spacer4 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.w = QtWidgets.QWidget(self)
        self.gbox = QtWidgets.QGridLayout(self.w)
        self.setCentralWidget(self.w)
        self.setStyleSheet('background-color: lightblue')
        self.setWindowIcon(QtGui.QIcon('Логотип ЗХ'))
        self.btnGet = QtWidgets.QPushButton('Добавить\nнового сотрудника')
        self.btnGet.setFixedHeight(100)
        self.btnGet.setStyleSheet('font-size: 25pt;font-family: Courier;background-color: rgb(0,170,210)')
        self.btnEdit = QtWidgets.QPushButton('Просмотреть и отредактировать\nданные сотрудника')
        self.btnEdit.setFixedHeight(100)
        self.btnEdit.setStyleSheet('font-size: 25pt;font-family: Courier;background-color: rgb(0,170,210)')
        self.btnDel = QtWidgets.QPushButton('Удалить\nданные сотрудника')
        self.btnDel.setFixedHeight(100)
        self.btnDel.setStyleSheet('font-size: 25pt;font-family: Courier;background-color: rgb(0,170,210)')
        self.btnAll = QtWidgets.QPushButton('Показать\nданные всех сотрудников')
        self.btnAll.setFixedHeight(100)
        self.btnAll.setStyleSheet('font-size: 25pt;font-family: Courier;background-color: rgb(0,170,210)')
        self.btnVac = QtWidgets.QPushButton('Показать\nсотрудников в отпуске')
        self.btnVac.setFixedHeight(100)
        self.btnVac.setStyleSheet('font-size: 25pt;font-family: Courier;background-color: rgb(0,170,210)')
        self.btnBirth = QtWidgets.QPushButton('Показать сотрудников с\nближайшими днями рождения')
        self.btnBirth.setFixedHeight(100)
        self.btnBirth.setStyleSheet('font-size: 25pt;font-family: Courier;background-color: rgb(0,170,210)')
        self.btnStat = QtWidgets.QPushButton('Показать статистику')
        self.btnStat.setFixedHeight(100)
        self.btnStat.setStyleSheet('font-size: 25pt;font-family: Courier;background-color: rgb(0,170,210)')
        self.btn = QtWidgets.QPushButton('Добавить отпуск')
        self.btn.setFixedHeight(100)
        self.btn.setStyleSheet('font-size: 25pt;font-family: Courier;background-color: rgb(0,170,210)')
        self.btnExit = QtWidgets.QPushButton('Выход')
        self.btnExit.setFixedHeight(100)
        self.btnExit.setStyleSheet('font-size: 25pt;font-family: Courier;background-color: rgb(0,170,210)')
        self.btnCsv = QtWidgets.QPushButton('Выгрузить\nданные в .csv')
        self.btnCsv.setFixedHeight(100)
        self.btnCsv.setStyleSheet('font-size: 25pt;font-family: Courier;background-color: rgb(0,170,210)')
        self.gbox.addItem(self.spacer1,0,0,1,4)
        self.gbox.addItem(self.spacer3,1,0,3,1)
        self.gbox.addWidget(self.btnGet,1,1)
        self.gbox.addWidget(self.btnEdit,1,2)
        self.gbox.addWidget(self.btnDel,1,3,1,2)
        self.gbox.addWidget(self.btnAll,2,1)
        self.gbox.addWidget(self.btnVac,2,2)
        self.gbox.addWidget(self.btnBirth,2,3,1,2)
        self.gbox.addWidget(self.btnStat,3,1)
        self.gbox.addWidget(self.btn,3,2)
        self.gbox.addWidget(self.btnExit,3,4,1,1)
        self.gbox.addWidget(self.btnCsv,3,3,1,1)
        self.gbox.addItem(self.spacer4,1,5,3,1)
        self.gbox.addItem(self.spacer2,4,0,1,4)
        self.btnGet.clicked.connect(self.openWin1)
        self.btnEdit.clicked.connect(self.openWin2)
        self.btnDel.clicked.connect(self.openWin3)
        self.btnAll.clicked.connect(self.openWin4)
        self.btnVac.clicked.connect(self.openWin5)
        self.btnBirth.clicked.connect(self.openWin6)
        self.btnStat.clicked.connect(self.openWin7)
        self.btn.clicked.connect(self.openWin8)
        self.btnCsv.clicked.connect(self.openWin9)
        self.btnExit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.show()
    def openWin1(self):
        self.openWin = Window1(self)
        self.openWin.show()
    @test_for_empty
    def openWin2(self):
            self.openWin = Window2(self)
            self.openWin.show()
    @test_for_empty
    def openWin3(self):
            self.openWin = Window3(self)
            self.openWin.show()
    @test_for_empty
    def openWin4(self):
            self.openWin = Window4(self)
            self.openWin.show()
    @test_for_empty
    def openWin5(self):
            self.openWin = Window5(self)
            self.openWin.show()
    @test_for_empty
    def openWin6(self):
            self.openWin = Window6(self)
            self.openWin.show()
    @test_for_empty
    def openWin7(self):
            self.openWin = Window7(self)
            self.openWin.show()
    @test_for_empty
    def openWin8(self):
            self.openWin = Window8(self)
            self.openWin.show()
    @test_for_empty
    def openWin9(self):
            self.openWin = Window9(self)
            self.openWin.show()
    def closeEvent(self, event):
        self.reply = QtWidgets.QMessageBox.question(self, 'Сообщение', "Выйти из программы?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        event.accept() if self.reply == QtWidgets.QMessageBox.Yes else event.ignore()