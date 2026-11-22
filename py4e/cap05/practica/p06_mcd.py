"""Ejercicio 6: Máximo común divisor con el algoritmo de Euclides."""

import math
def mcd(a: int, b: int) -> int:
    """Devuelve el máximo común divisor con el algoritmo de Euclides."""
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    assert mcd(48, 18) == 6
    assert mcd(17, 5) == 1
    assert mcd(48, 18) == math.gcd(48, 18)
    print('Todas las pruebas pasan')
