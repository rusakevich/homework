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

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tunning()
    def tunning(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('База сотрудников')
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
        self.gbox = QtWidgets.QGridLayout()
        self.btnCsv = QtWidgets.QPushButton('Выгрузить\nданные в .csv')
        self.btnCsv.setFixedHeight(100)
        self.btnCsv.setStyleSheet('font-size: 25pt;font-family: Courier;background-color: rgb(0,170,210)')


        self.gbox.addWidget(self.btnGet,0,0)
        self.gbox.addWidget(self.btnEdit,0,1)
        self.gbox.addWidget(self.btnDel,0,2,1,2)
        self.gbox.addWidget(self.btnAll,1,0)
        self.gbox.addWidget(self.btnVac,1,1)
        self.gbox.addWidget(self.btnBirth,1,2,1,2)
        self.gbox.addWidget(self.btnStat,2,0)
        self.gbox.addWidget(self.btn,2,1)
        self.gbox.addWidget(self.btnExit,2,3,1,1)
        self.gbox.addWidget(self.btnCsv,2,2,1,1)
        self.setLayout(self.gbox)
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