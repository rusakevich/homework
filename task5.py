def fourth(x):
    if x > 0:
        f = lambda y: 'I' if y > 0 else 'IV'
    elif x < 0:
        f = lambda y: 'II' if y > 0 else 'III'
    return f

x = int(input('X='))
while x == 0:
    x = int(input('Введите отличное значение от нуля для X: '))
y = int(input('Y='))
while y == 0:
    y = int(input('Введите отличное значение от нуля для Y: '))
print('Номер четверти: {}'.format(fourth(x)(y)))