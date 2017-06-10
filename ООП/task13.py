class Human(object):
    '''Класс человек - общий для учеников и учителей'''
    def __init__(self, lastname, firstname, age):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age


class Information(object):
    '''Банк знаний'''
    def __init__(self, info):
        self.info = info
    def addinfo(self, newinfo):
        self.info += newinfo
    def exportinfo(self, i):
        return self.info[i]
    def printinfo(self):
        print('Доступная информация для обучения: {}'.format(', '.join(self.info)))


class Teacher(Human):
    '''Учитель умеет брать знания из банка знаний и обучать учеников'''
    def __init__(self, lastname, firstname, age):
        super().__init__(lastname, firstname, age)
        self.pupils = []
    def inward(self, info):
        self.info = info
    def outwards(self):
        return self.info
    def printinfo(self):
        print('Учитель {} {} {} лет готов обучать: {}'.format(self.lastname, self.firstname, self.age, self.info))
    def addpupil(self, pupil):
        self.pupils.append('{} {} {} лет'.format(pupil.lastname, pupil.firstname, pupil.age))
        self.amountpupils = len(self.pupils)
    def printpupils(self):
        print('У учителя {} {} есть ученики: {}'.format(self.lastname, self.firstname, ', '.join(self.pupils)))


class Pupil(Human):
    '''Ученик умеет получать знания у учителя и накапливать их'''
    def __init__(self, lastname, firstname, age):
        super().__init__(lastname, firstname, age)
        self.gentlefolks = []
    def getinfo(self, info):
        self.gentlefolks.append(info)
    def printinfo(self):
        print('Ученик {} {} {} лет знает: {}'.format(self.lastname, self.firstname, self.age, ', '.join(self.gentlefolks)))


class Course(object):
    '''Класс курсы - получает информацию об учителе, может выводить кол-во обучающихся учеников'''
    def __init__(self, coursename, teacher):
        self.coursename = coursename
        self.teachername = '{} {}'.format(teacher.lastname, teacher.firstname)
        self.amountpupils = teacher.amountpupils
    def printinfo(self):
        print('Курсы {} ведет {}'.format(self.coursename, self.teachername))
        print('На курсах по {} учится {} ученик(ов)'.format(self.coursename, self.amountpupils))




#Внесем знания в банк знаний
info = Information(['PyQt5', 'ООП', 'Functions', 'GIT'])
info.addinfo(['SQLite', 'Generators'])

#Инициализируем учеников
pupil1 = Pupil("Иванов", "Иван", 20)
pupil2 = Pupil('Гаврилов', 'Фёдор', 25)
pupil3 = Pupil('Егорова', 'Надежда', 22)

#Инициализируем учителя
teacher1 = Teacher("Петров", "Роман", 30)

#Добавим учителю учеников
teacher1.addpupil(pupil1)
teacher1.addpupil(pupil2)
teacher1.addpupil(pupil3)

#Инициализируем курс обучения
course1 = Course('Python', teacher1)

#Обучим учеников
teacher1.inward(info.exportinfo(2))
pupil1.getinfo(teacher1.outwards())
pupil2.getinfo(teacher1.outwards())
pupil3.getinfo(teacher1.outwards())

teacher1.inward(info.exportinfo(5))
pupil1.getinfo(teacher1.outwards())
pupil2.getinfo(teacher1.outwards())

teacher1.inward(info.exportinfo(3))
pupil3.getinfo(teacher1.outwards())

#Выведем информацию по всем имеющимся объектам
info.printinfo()
course1.printinfo()
teacher1.printinfo()
teacher1.printpupils()
pupil1.printinfo()
pupil2.printinfo()
pupil3.printinfo()