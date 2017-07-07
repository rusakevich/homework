#print(list(range(1,10)))
from coursework import *


with db_session:
    b=[]
    a = select(c for c in Employee)
    for i in a:
        b.append('{} {} {} {}'.format(i.surname,i.name,i.patronymic,i.birthdate))
    print(b)

#d = ('1','2','3')
#print(' '.join(d))
