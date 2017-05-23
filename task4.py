def polindrom(stroka):
    return True if stroka == stroka[::-1] else False

s = input('Введите строку: ')
print(polindrom(s))