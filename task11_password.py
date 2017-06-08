from random import randint
from task12_pause import pause


@pause(int(input('Введите на сколько секунд задерживаем выполнение функции: ')))
def password_generator(n):
    while 1:
        i = 1
        p = []
        while i <= n:
            p.append(chr(randint(33,126)))
            i += 1
        yield ''.join(p) 
        

gen = password_generator(int(input('Введите длину пароля: ')))
print('Случайный пароль №1: {}'.format(next(gen)))
print('Случайный пароль №2: {}'.format(next(gen)))
print('Случайный пароль №3: {}'.format(next(gen)))
