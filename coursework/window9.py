from os import path
from PyQt5 import QtWidgets, QtCore
from base import *
from __init__ import message_info, message_warning


class Window9(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.tunning()
    def tunning(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Выгрузка данных')
        self.label_unload = QtWidgets.QLabel('Выберите поля для выгрузки:')
        self.label_directory = QtWidgets.QLabel(path.split(__file__)[0])
        self.btnUnload = QtWidgets.QPushButton('Выгрузить')
        self.btnExit = QtWidgets.QPushButton('Закрыть')
        self.btndirectory = QtWidgets.QPushButton('Директория')
        self.btnUnload.setToolTip('Выгрузить выбранные поля')
        self.btnExit.setToolTip('Закрыть')
        self.btndirectory.setToolTip('Выберите директорию сохранения файла')
        self.cbkey = QtWidgets.QCheckBox('Ключ')
        self.cbsurname = QtWidgets.QCheckBox('Фамилия')
        self.cbsurname.setChecked(True)
        self.cbname = QtWidgets.QCheckBox('Имя')
        self.cbname.setChecked(True)
        self.cbpatronymic = QtWidgets.QCheckBox('Отчество')
        self.cbbirthdate = QtWidgets.QCheckBox('Дата рождения')
        self.cbsex = QtWidgets.QCheckBox('Пол')
        self.cbphone = QtWidgets.QCheckBox('Телефон')
        self.cbphone.setChecked(True)
        self.cbemail = QtWidgets.QCheckBox('Электронная почта')
        self.cbemail.setChecked(True)
        self.cbpost = QtWidgets.QCheckBox('Должность')
        self.cbpost.setChecked(True)
        self.cbdepartment = QtWidgets.QCheckBox('Отдел')
        self.cbdepartment.setChecked(True)
        self.cbdate_of_recruitment = QtWidgets.QCheckBox('Дата приёма на работу')
        self.cbmarital_status = QtWidgets.QCheckBox('Семейное положение')
        self.cbdate_start_vacation = QtWidgets.QCheckBox('Дата начала отпуска')
        self.cbdate_finish_vacation = QtWidgets.QCheckBox('Дата окончания отпуска')
        self.cbkind_vacation = QtWidgets.QCheckBox('Вид отпуска')
        self.gbox = QtWidgets.QGridLayout()
        self.gbox.addWidget(self.label_unload,0,0)
        self.gbox.addWidget(self.cbkey,1,0)
        self.gbox.addWidget(self.cbsurname,2,0)
        self.gbox.addWidget(self.cbname,3,0)
        self.gbox.addWidget(self.cbpatronymic,4,0)
        self.gbox.addWidget(self.cbbirthdate,5,0)
        self.gbox.addWidget(self.cbsex,6,0)
        self.gbox.addWidget(self.cbphone,7,0)
        self.gbox.addWidget(self.cbemail,8,0)
        self.gbox.addWidget(self.cbpost,9,0)
        self.gbox.addWidget(self.cbdepartment,10,0)
        self.gbox.addWidget(self.cbdate_of_recruitment,11,0)
        self.gbox.addWidget(self.cbmarital_status,12,0)
        self.gbox.addWidget(self.cbdate_start_vacation,13,0)
        self.gbox.addWidget(self.cbdate_finish_vacation,14,0)
        self.gbox.addWidget(self.cbkind_vacation,15,0)
        self.gbox.addWidget(self.btnUnload,16,0)
        self.gbox.addWidget(self.btnExit,17,0)
        self.gbox.addWidget(self.btndirectory,18,0)
        self.gbox.addWidget(self.label_directory,19,0)
        self.setLayout(self.gbox)
        self.btnExit.clicked.connect(self.close)
        self.btnUnload.clicked.connect(self.unloadverify)
        self.btndirectory.clicked.connect(self.directory)
    def directory(self):
        self.directory = QtWidgets.QFileDialog.getExistingDirectory()
        self.label_directory.setText(self.directory)
    def unloadverify(self):
        message_warning(self, 'Выделите хотя бы одно поле') if (not self.cbkey.isChecked() and not self.cbsurname.isChecked() and not self.cbname.isChecked() and
                                                                not self.cbpatronymic.isChecked() and not self.cbbirthdate.isChecked() and not self.cbsex.isChecked() and
                                                                not self.cbphone.isChecked() and not self.cbemail.isChecked() and not self.cbpost.isChecked() and
                                                                not self.cbdepartment.isChecked() and not self.cbdate_of_recruitment.isChecked() and not self.cbmarital_status.isChecked() and
                                                                not self.cbdate_start_vacation.isChecked() and not self.cbdate_finish_vacation.isChecked() and not self.cbkind_vacation.isChecked()) else self.unload()
    def unload(self):
        try:
            with open('{}/{}'.format(self.label_directory.text(),'base.csv'), 'w') as f:
                f.write('Ключ;') if self.cbkey.isChecked() else None
                f.write('Фамилия;') if self.cbsurname.isChecked() else None
                f.write('Имя;') if self.cbname.isChecked() else None
                f.write('Отчество;') if self.cbpatronymic.isChecked() else None
                f.write('Дата рождения;') if self.cbbirthdate.isChecked() else None
                f.write('Пол;') if self.cbsex.isChecked() else None
                f.write('Номер телефона;') if self.cbphone.isChecked() else None
                f.write('Электронная почта;') if self.cbemail.isChecked() else None
                f.write('Должность;') if self.cbpost.isChecked() else None
                f.write('Отдел;') if self.cbdepartment.isChecked() else None
                f.write('Дата приема на работу;') if self.cbdate_of_recruitment.isChecked() else None
                f.write('Семейное положение;') if self.cbmarital_status.isChecked() else None
                f.write('Дата начала отпуска;') if self.cbdate_start_vacation.isChecked() else None
                f.write('Дата окончания отпуска;') if self.cbdate_finish_vacation.isChecked() else None
                f.write('Вид отпуска;') if self.cbkind_vacation.isChecked() else None
                f.write('\n')
                with db_session:
                    self.records = select(c for c in Employee)
                    for i in list(self.records):
                        f.write(str(i.key)+';') if self.cbkey.isChecked() else None
                        f.write(str(i.surname)+';') if self.cbsurname.isChecked() else None
                        f.write(str(i.name)+';') if self.cbname.isChecked() else None
                        f.write(str(i.patronymic)+';') if self.cbpatronymic.isChecked() else None
                        f.write(str(i.birthdate)+';') if self.cbbirthdate.isChecked() else None
                        f.write(str(i.sex)+';') if self.cbsex.isChecked() else None
                        f.write(str(i.phone)+';') if self.cbphone.isChecked() else None
                        f.write(str(i.email)+';') if self.cbemail.isChecked() else None
                        f.write(str(i.post)+';') if self.cbpost.isChecked() else None
                        f.write(str(i.department)+';') if self.cbdepartment.isChecked() else None
                        f.write(str(i.date_of_recruitment)+';') if self.cbdate_of_recruitment.isChecked() else None
                        f.write(str(i.marital_status)+';') if self.cbmarital_status.isChecked() else None
                        f.write(str(i.date_start_vacation)+';') if self.cbdate_start_vacation.isChecked() else None
                        f.write(str(i.date_finish_vacation)+';') if self.cbdate_finish_vacation.isChecked() else None
                        f.write(str(i.kind_vacation)+';') if self.cbkind_vacation.isChecked() else None
                        f.write('\n')
                        message_info(self, 'Данные выгружены')
        except PermissionError:
            message_warning(self, 'Закройте файл .csv')