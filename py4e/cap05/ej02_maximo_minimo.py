"""Ejercicios 2: Maximo y minimo sin usar max() ni min()."""

mayor = None
menor = None

while True:
    entrada = input("Ingresa un numero: ")
    if entrada == "done":
        break
    try:
        numero = float(entrada)
    except ValueError:
        print("Invalid input")
        continue
    if mayor is None or numero > mayor:
        mayor = numero
    if menor is None or numero < menor:
        menor = numero
        
print(mayor, menor)
    