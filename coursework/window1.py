from PyQt5 import QtWidgets, QtCore, Qt
from base import *
from __init__ import warning, message_warning, message_info


class Window1(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.tunning()
    def tunning(self):
        self.setWindowTitle('Завести нового сотрудника')
        self.spacer1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.spacer2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.spacer3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.spacer4 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.btnSave = QtWidgets.QPushButton('Добавить')
        self.btnExit = QtWidgets.QPushButton('Закрыть')
        self.btnSaveExit = QtWidgets.QPushButton('Добавить и закрыть')
        self.btnSave.setMinimumWidth(400)
        self.btnSave.setToolTip('Добавить данные сотрудника')
        self.btnSaveExit.setToolTip('Добавить данные сотрудника и закрыть')
        self.btnExit.setToolTip('Закрыть')
        self.label_surname = QtWidgets.QLabel('Фамилия')
        self.label_name = QtWidgets.QLabel('Имя')
        self.label_patronymic = QtWidgets.QLabel('Отчество')
        self.label_birthdate = QtWidgets.QLabel('Дата рождения')
        self.label_sex = QtWidgets.QLabel('Пол')
        self.label_phone = QtWidgets.QLabel('Номер телефона')
        self.label_email = QtWidgets.QLabel('Электронная почта')
        self.label_post = QtWidgets.QLabel('Должность')
        self.label_department = QtWidgets.QLabel('Отдел')
        self.label_date_of_recruitment = QtWidgets.QLabel('Дата приёма на работу')
        self.label_marital_status = QtWidgets.QLabel('Семеное положение')
        self.line_surname = QtWidgets.QLineEdit()
        self.line_surname.setPlaceholderText('Иванов')
        self.line_surname.setToolTip('Введите фамилию')
        self.line_name = QtWidgets.QLineEdit()
        self.line_name.setPlaceholderText('Иван')
        self.line_name.setToolTip('Введите имя')
        self.line_patronymic = QtWidgets.QLineEdit()
        self.line_patronymic.setPlaceholderText('Иванович')
        self.line_patronymic.setToolTip('Введите отчество')
        self.line_birthdate = QtWidgets.QDateEdit()
        self.line_birthdate.setToolTip('Выберите дату рождения')
        self.line_sex = Qt.QComboBox()
        self.line_sex.addItems(['Мужской','Женский'])
        self.line_sex.setToolTip('Выберите пол')
        self.line_phone = QtWidgets.QLineEdit()
        self.line_phone.setInputMask('+7(000)0000000')
        self.line_phone.setToolTip('Введите номер телефона')
        self.line_email = QtWidgets.QLineEdit()
        self.line_email.setPlaceholderText('example@example.com')
        self.line_email.setToolTip('Введите адрес электронной почты')
        self.line_post = QtWidgets.QLineEdit()
        self.line_post.setToolTip('Введите название должности')
        self.line_department = QtWidgets.QLineEdit()
        self.line_department.setToolTip('Введите название отдела')
        self.line_date_of_recruitment = QtWidgets.QDateEdit()
        self.line_date_of_recruitment.setToolTip('Выберите дату приёма на работу')
        self.line_marital_status = Qt.QComboBox()
        self.line_marital_status.addItems(['Женат','Не женат','Замужем','Не замужем'])
        self.line_marital_status.setToolTip('Выберите семейное положение')
        self.gbox = QtWidgets.QGridLayout(self)
        self.gbox.addItem(self.spacer1,0,0,1,2)
        self.gbox.addItem(self.spacer3,1,0,13,1)
        self.gbox.addWidget(self.label_surname,1,1)
        self.gbox.addWidget(self.label_name,2,1)
        self.gbox.addWidget(self.label_patronymic,3,1)
        self.gbox.addWidget(self.label_birthdate,4,1)
        self.gbox.addWidget(self.label_sex,5,1)
        self.gbox.addWidget(self.label_phone,6,1)
        self.gbox.addWidget(self.label_email,7,1)
        self.gbox.addWidget(self.label_post,8,1)
        self.gbox.addWidget(self.label_department,9,1)
        self.gbox.addWidget(self.label_date_of_recruitment,10,1)
        self.gbox.addWidget(self.label_marital_status,11,1)
        self.gbox.addWidget(self.line_surname,1,2)
        self.gbox.addWidget(self.line_name,2,2)
        self.gbox.addWidget(self.line_patronymic,3,2)
        self.gbox.addWidget(self.line_birthdate,4,2)
        self.gbox.addWidget(self.line_sex,5,2)
        self.gbox.addWidget(self.line_phone,6,2)
        self.gbox.addWidget(self.line_email,7,2)
        self.gbox.addWidget(self.line_post,8,2)
        self.gbox.addWidget(self.line_department,9,2)
        self.gbox.addWidget(self.line_date_of_recruitment,10,2)
        self.gbox.addWidget(self.line_marital_status,11,2)
        self.gbox.addWidget(self.btnSave,12,1,1,2)
        self.gbox.addWidget(self.btnExit,13,2)
        self.gbox.addWidget(self.btnSaveExit,13,1)
        self.gbox.addItem(self.spacer4,1,3,13,1)
        self.gbox.addItem(self.spacer2,14,0,1,2)
        self.btnSave.clicked.connect(self.saveall)
        self.btnSaveExit.clicked.connect(self.saveallexit)
        self.btnExit.clicked.connect(self.close)
    def save(self):
        with db_session:
            self.a = Employee(surname=self.line_surname.text(), name=self.line_name.text(), patronymic=self.line_patronymic.text(), birthdate=self.line_birthdate.text() , date_of_recruitment=self.line_date_of_recruitment.text())
            self.a.sex = self.line_sex.currentText()
            self.a.phone = self.line_phone.text()
            self.a.email = self.line_email.text()
            self.a.post = self.line_post.text()
            self.a.department = self.line_department.text()
            self.a.marital_status = self.line_marital_status.currentText()
            self.line_surname.clear()
            self.line_name.clear()
            self.line_patronymic.clear()
            self.line_phone.clear()
            self.line_post.clear()
            self.line_department.clear()
            self.line_email.clear()
            message_info(self, 'Данные сотрудника добавлены')
    def saveall(self):
        message_warning(self, 'Заполнены не все обязательные поля') if warning(self) else self.save()
    def saveallexit(self):
        message_warning(self, 'Заполнены не все обязательные поля') if warning(self) else (self.save(), self.close()) 
    