from os import path

f = './params.txt'
params = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': 'val3'
    }

##################################

'''ФУНКЦИОНАЛЬНЫЙ МЕТОД'''


def read_params(source):
    """Функция чтения - при каждом новом формате в elif добавляем новый метод чтения"""
    params = {}
    a, b = path.splitext(source)
    if b == '.txt':
        '''Читаем текстовые параметры из source'''
    elif b == '.format_1':
        '''Читаем для format_1 параметры из source'''
    elif b == '.format_2':
        '''Читаем для format_2 параметры из source'''
    else:
        return 'Не прочитано - формат не распознан'
    return params


def write_params(source, params):
    """Функция записи - при каждом новом формате в elif добавляем новый метод записи"""
    a, b = path.splitext(source)
    if b == '.txt':
        '''Записываем текстовые параметры в source'''
    elif b == '.format_1':
        '''Записываем для format_1 параметры в source'''
    elif b == '.format_2':
        '''Записываем для format_2 параметры в source'''
    else:
        return 'Не записано - формат не распознан'





write_params(f, params)
print(read_params(f))



###########################################
###########################################
###########################################
'''МЕТОД ООП'''
'''При появлении нового формата необходимо добавить методы чтения и записи в соответствующие подклассы, 
а в суперкласс добавить в словарь название формата и метода(ключ: значение)'''


class Identifier(object):
    """Суперкласс идентификатор для определения формата переданного файла и координации метода чтения/записи"""
    def set(self, source):
        self.a, self.formatfile = path.splitext(source)
        self.d = {
            '.txt': metod_txt,
            '.format_1': metod_2,
            '.format_2': metod_3
             }



class Reader(Identifier):
    """Подкласс суперкласса идентификатор - для ввода имени файла, чтения файла и вывода полученной информации из файла, содержит методы чтения"""
    def set(self, source):
        super().set(source)
        self.source = source
        self.params = {}

    def metod_txt(self):
        '''Читаем текстовые параметры из source'''
    def metod_1(self):
        '''Читаем для format_1 параметры из source'''
    def metod_2(self):
        '''Читаем для format_2 параметры из source'''
    def readfile(self):
        self.self.d.get(self.formatfile)()

    def get(self):
        return self.params



class Writer(Identifier):
    """Подкласс суперкласса идентификатор - для ввода имени файла и информации для записи, а так же для записи в файл, содержит методы записи"""
    def set(self, source, params):
        super().set(source)
        self.params = params
        self.source = source

    def metod_txt(self):
        '''Записываем текстовые параметры в source'''
    def metod_1(self):
        '''Записываем для format_1 параметры в source'''
    def metod_2(self):
        '''Читаем для format_2 параметры в source'''
    def writefile(self):
        self.self.d.get(self.formatfile)()




reader = Reader() #Создаем объект читатель
writer = Writer() #Создаем объект писатель

reader.set(f) #Передаем читателю имя файла
reader.readfile() #Читаем файл
print(reader.get()) #Выводим прочитанную информацию на экран

writer.set(f, params) #Передаем писателю имя файла и инфо для записи в файл
writer.writefile() #Записываем в файл инфо