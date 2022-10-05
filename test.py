from Controller import *


xy = amplitudHoraria(15,20)

y = quitarHorario (16,17,xy)

x = quitarHorario(16,17.30,y)

h = horasPosibles(1.00, x)


print(y)
print(x)
print(h)