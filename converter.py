import sys
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QDoubleSpinBox, QPushButton, QGridLayout
from yahoo_finance import Currency

class Course(QObject):
    def get(self):
        return float(Currency('USDRUB').get_bid())


class CurrencyConverter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initUi()
        self._initLayout()
        self._initSignals()

    def _initUi(self):
        self.setWindowTitle('Конвертер валют')
        self.courseusd = QLabel('Курс доллара на бирже:', self)
        self.courseusddisp = QLabel(self)
        self.saleusd = QLabel('Курс продажи доллара:', self)
        self.saleusddisp = QLabel(self)
        self.buyusd = QLabel('Курс покупки доллара:', self)
        self.buyusddisp = QLabel(self)
        self.scrlabel = QLabel('Сумма в рублях:', self)
        self.rezultlabel = QLabel('Сумма в долларах:', self)
        self.scrAmount = QDoubleSpinBox(self)
        self.scrAmount.setMaximum(999999999)
        self.rezultAmount = QDoubleSpinBox(self)
        self.rezultAmount.setMaximum(999999999)
        self.convertBtn = QPushButton('Перевести', self)
        self.clearBtn = QPushButton('Очистить', self)
        self.updateConvertBtnStatus()
        self.courseusddisp.setText(str(Course().get()))
        saleusdvalue = self.saleusddisp.setText(str(round(Course().get()*1.006, 2)))
        buyusdvalue = self.buyusddisp.setText(str(round(Course().get()/1.006, 2)))

    def _initLayout(self):
        w = QWidget(self)
        self.mainLayout = QGridLayout(w)
        self.mainLayout.addWidget(self.courseusd, 0, 0)
        self.mainLayout.addWidget(self.courseusddisp, 0, 1)
        self.mainLayout.addWidget(self.saleusd, 1, 0)
        self.mainLayout.addWidget(self.saleusddisp, 1, 1)
        self.mainLayout.addWidget(self.buyusd, 2, 0)
        self.mainLayout.addWidget(self.buyusddisp, 2, 1)
        self.mainLayout.addWidget(self.scrlabel, 3, 0)
        self.mainLayout.addWidget(self.scrAmount, 3, 1)
        self.mainLayout.addWidget(self.rezultlabel, 4, 0)
        self.mainLayout.addWidget(self.rezultAmount, 4, 1)
        self.mainLayout.addWidget(self.convertBtn, 5, 0, 1, 2)
        self.mainLayout.addWidget(self.clearBtn, 6, 0, 1, 2)
        self.setCentralWidget(w)

    def _initSignals(self):
        self.convertBtn.clicked.connect(self.onClick)
        self.clearBtn.clicked.connect(self.onClear)
        self.scrAmount.valueChanged.connect(self.updateConvertBtnStatus)
        self.rezultAmount.valueChanged.connect(self.updateConvertBtnStatus)

    def onClick(self):
        cours = Course().get()
        self.courseusddisp.setText(str(cours))
        saleusdvalue = round(cours*1.006, 2)
        self.saleusddisp.setText(str(saleusdvalue))
        buyusdvalue = round(cours/1.006, 2)
        self.buyusddisp.setText(str(buyusdvalue))
        valuerub = self.scrAmount.value()
        valueusd = self.rezultAmount.value()
        if valuerub != 0 and valueusd == 0:
            self.rezultAmount.setValue(valuerub / saleusdvalue)
        elif valuerub == 0 and valueusd != 0:
            self.scrAmount.setValue(valueusd * buyusdvalue)

    def onClear(self):
        self.rezultAmount.setValue(0)
        self.scrAmount.setValue(0)

    def updateConvertBtnStatus(self):
        valuerub = self.scrAmount.value()
        valueusd = self.rezultAmount.value()
        self.convertBtn.setEnabled(bool(valuerub) ^ bool(valueusd))
if __name__ == '__main__':

    app = QApplication(sys.argv)
    converter = CurrencyConverter()
    converter.show()

    sys.exit(app.exec_())

