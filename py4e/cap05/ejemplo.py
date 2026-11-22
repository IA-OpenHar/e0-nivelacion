"""Ejemplo del capitulo 5."""

amigos = ['Joseph', 'Glenn', 'Sally']
for amigo in amigos:
    print('Feliz año nuevo,', amigo)
    
for i in range(3):
    print('vuelta', i)

numeros = [3, 41, 12, 9, 74, 15]
conteo = 0
total = 0
mayor = None
for x in numeros:
    conteo = conteo + 1
    total = total + x
    if mayor is None or x > mayor:
        mayor = x
print(conteo, total, mayor)
