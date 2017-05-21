Plate = int(input('Введите количество тарелок: '))
Det = float(input('Введите количество моющего средства: '))
Cons = float(input('Введите количество расходуемого средства на 1 тарелку: '))

A = Det
i = 0
print('Моющее средство после каждого мытья:')
while i <= Plate and A - Cons > 0:
    print(A-Cons, end = ' | ')
    A -= Cons
    i += i
    
print('\n')
if Det/Cons > Plate:
    print('Осталось моющего средства:', Det - Plate * Cons)
elif Det/Cons < Plate:
    print('Осталось не вымытых тарелок:', int(Plate - Det/Cons))
elif Det/Cons == Plate:
    print('Тарелок и моющего средства не осталось')