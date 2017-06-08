from random import randint
from time import sleep

def pause(sec):
    '''Декоратор задержки выполнения функций'''
    def decorator(func):
            def wrapper(*args,**kwargs):
                print('Ждём {} секунд(ы)...'.format(sec))
                sleep(sec)
                print('Прошло {} секунд(ы), результат выполненной функции:'.format(sec))
                return func(*args,**kwargs)
            return wrapper
    return decorator