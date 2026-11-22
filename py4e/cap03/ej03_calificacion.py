import sys

try:
    puntuacion = float(input('Introduce una puntuacion entre 0.0 y 1.0: '))
except ValueError:
    print('Puntuacion incorrecta')
    sys.exit(1)
    
if puntuacion < 0.0 or puntuacion > 1.0:
    print('Bad score')
elif puntuacion >= 0.9:
    print('A')
elif puntuacion >= 0.8:
    print('B')
elif puntuacion >= 0.7:
    print('C')
elif puntuacion >= 0.6:
    print('D')
else:
    print('F')