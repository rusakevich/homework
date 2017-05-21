#Vertex A
x1 = float(input('X1 = '))
y1 = float(input('Y1 = '))
#Vertex B
x2 = float(input('X2 = '))
y2 = float(input('Y2 = '))
#Vertex C
x3 = float(input('X3 = '))
y3 = float(input('Y3 = '))

AB = ((x1-x2)**2+(y1-y2)**2)**0.5
AC = ((x1-x3)**2+(y1-y3)**2)**0.5
BC = ((x3-x2)**2+(y3-y2)**2)**0.5

print('Triangle is rectangular') if AB**2 == AC**2 + BC**2 or AC**2 == AB**2 + BC**2 or BC**2 == AB**2 + AC**2 else print('Triangle is not rectangular')