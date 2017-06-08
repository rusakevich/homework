from random import randint
from task12_pause import pause


@pause(int(input('Введите на сколько секунд задерживаем выполнение функции: ')))
def password_generator(n):
    #sign = list(set.union(set(range(48,57)),set(range(32,90)), set(range(97,122))))
    i = 1
    while i <= n:
        yield chr(randint(33,126))
        i += 1

password_generator(int(input('Введите длину пароля: ')))

