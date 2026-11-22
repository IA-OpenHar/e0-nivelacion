"""Ejercicio 1; Total, conteo y promedio con manejo de errores."""

conteo = 0
total = 0.0

while True:
    entrada = input("Ingresa un numero: ")
    if entrada == "done":
        break
    try:
        numero = float(entrada)
    except ValueError:
        print("Invalid input")
        continue
    
    conteo = conteo + 1
    total = total + numero
    
if conteo > 0:
    promedio = total / conteo
else:
    promedio = 0
    
print(total, conteo, promedio)
