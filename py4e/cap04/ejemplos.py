"""Ejemplos de funciones integrdas, modulos y definiciones propias (Cap. 4)"""

import math
import random


def calcular_area(base, altura):
    """Calcula y devuelve el area de un triangulo."""
    area = base * altura / 2
    return area


def saludar(nombre):
    """Imprime un saludo sin devolver valor (funcion void)."""
    print('Hola', nombre)
    
def main():
    """Ejecuta todos los ejemplos del capitulo 4."""
    # --- A. Funciones integradas y conversion ---
    print(max('Hello world'))   # w: el carácter "mayor"
    print(len('Hello world'))   # 11
    print(int(3.99999))         # 3: int() corta los decimales, no redondea
    print(int(-2.3))            # -2
    print(float('3.14159'))     # 3.14159
    print(str(32))              # 32, ahora como texto

    # --- B. El modulo math ---
    grados = 45
    radianes = grados / 360.0 * 2 * math.pi  # sin(), cos() y tan() trabajan en radianes
    print(math.sin(radianes))                # 0.7071067811865476
    print(math.sqrt(2) / 2.0)                # el mismo valor: comprobación cruzada

    # --- C. Numeros pseudoaleatorios ---
    random.seed(42)              # semilla fija: el mismo resultado en cada ejecución
    print(random.random())       # float entre 0.0 y 1.0 (sin incluir 1.0)
    print(random.randint(5, 10)) # entero entre 5 y 10, ambos incluidos

    # --- D. Definir tus propias funciones ---
    resultado = calcular_area(10, 4)  # 10 y 4 son los argumentos
    print(resultado)                  # 20.0

# pylint: disable=assignment-from-no-return
valor = saludar('Har')            # imprime Hola Har 
print(valor)                      # none: saludar() no tiene return


if __name__ == '__main__':
    main()
