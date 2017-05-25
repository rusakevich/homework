def Reckoning_into_10(x, n):
    """Перевод из n-й системы счисления в 10-ю"""
    LSTx = list(str(x))
    for k in range(len(LSTx)):
        LSTx[k] = 10 if LSTx[k] == 'a' else LSTx[k]
        LSTx[k] = 11 if LSTx[k] == 'b' else LSTx[k]
        LSTx[k] = 12 if LSTx[k] == 'c' else LSTx[k]
        LSTx[k] = 13 if LSTx[k] == 'd' else LSTx[k]
        LSTx[k] = 14 if LSTx[k] == 'e' else LSTx[k]
        LSTx[k] = 15 if LSTx[k] == 'f' else LSTx[k]

    for i in range(len(LSTx)):
        LSTx[i] = int(LSTx[i])
        if LSTx[i] > n - 1:
            return 'Attention!!! Это не {}-я система данных!!!'.format(n)
    LSTx = LSTx[::-1]
    X = 0
    for j in range(len(LSTx)):
        X += LSTx[j] * (n ** j)
    return X

def Reckoning_from_10(x, n):
    """Перевод из десятичной системы в n-ю"""
    x = int(x)
    X = ''
    while x > n:
        ost = x % n
        x = x // n
        ost = 'a' if ost == 10 else ost
        ost = 'b' if ost == 11 else ost
        ost = 'c' if ost == 12 else ost
        ost = 'd' if ost == 13 else ost
        ost = 'e' if ost == 14 else ost
        ost = 'f' if ost == 15 else ost

        X += str(ost)

        ost = 10 if ost == 'a' else ost
        ost = 11 if ost == 'b' else ost
        ost = 12 if ost == 'c' else ost
        ost = 13 if ost == 'd' else ost
        ost = 14 if ost == 'e' else ost
        ost = 15 if ost == 'f' else ost

    ost = x % n
    ost = 'a' if ost == 10 else ost
    ost = 'b' if ost == 11 else ost
    ost = 'c' if ost == 12 else ost
    ost = 'd' if ost == 13 else ost
    ost = 'e' if ost == 14 else ost
    ost = 'f' if ost == 15 else ost

    x = x // n
    x = 'a' if x == 10 else x
    x = 'b' if x == 11 else x
    x = 'c' if x == 12 else x
    x = 'd' if x == 13 else x
    x = 'e' if x == 14 else x
    x = 'f' if x == 15 else x

    X += str(ost) + str(x) if x!=0 else str(ost)
    #print(x)
    return X[::-1]



a = int(input('Введите систему счисления, из которой будем переводить: '))
b = input('Введите число в {}-й системе счисления для перевода в 10-ю: '.format(a))

print(Reckoning_into_10(b,a))

d = input('Введите десятичное число: ')
c = int(input('Введите систему счисления, в которую будем переводить: '))

print(Reckoning_from_10(d,c))