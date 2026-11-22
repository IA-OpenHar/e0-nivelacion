"""Ejercicio 9: Juego de adivinanza con semilla fija y contador de intentos."""

import random

def jugar_adivina() -> int:
    """Juego de adivinanza con semilla 42. Devuelve el número de intentos."""
    random.seed(42)
    secreto = random.randint(1, 100)
    intentos = 0

    while True:
        entrada = input("Adivina el número (1-100): ")
        try:
            num = int(entrada)
        except ValueError:
            print("Entrada inválida")
            continue

        intentos += 1
        if num == secreto:
            print(f"¡Acertaste en {intentos} intentos!")
            break
        if num < secreto:
            print("Más alto")
        else:
            print("Más bajo")

    return intentos

if __name__ == '__main__':
    jugar_adivina()
