def fibonacci(d):
    n = 0
    k = 1
    yield str(k)
    i = 0
    while i < d-1:
        n += k
        yield str(n)
        i += 2
        if i < d:
            k += n
            yield str(k)


print(' '.join(list(fibonacci(int(input('Введите количество элементов ряда Фибоначчи: '))))))