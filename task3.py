#Vertex A
x1 = float(input('X1 = '))
y1 = float(input('Y1 = '))
#Vertex B
x2 = float(input('X2 = '))
y2 = float(input('Y2 = '))
#Vertex C
x3 = float(input('X3 = '))
y3 = float(input('Y3 = '))

#Length in square
AB = (x1-x2)**2+(y1-y2)**2
AC = (x1-x3)**2+(y1-y3)**2
BC = (x3-x2)**2+(y3-y2)**2

print('Triangle is rectangular') if AB == AC + BC or AC == AB + BC or BC == AB + AC else print('Triangle is not rectangular')