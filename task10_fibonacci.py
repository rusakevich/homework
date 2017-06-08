def fibonacci(d):
    n = 0
    k = 1
    yield k
    i = 0
    while i < d-1:
        n += k
        yield n
        i += 2
        if i < d:
            k += n
            yield k

f = (str(i) for i in fibonacci(int(input('Введите количество элементов ряда Фибоначчи: '))))
print(' '.join(list(f)))