"""Ejercicio 10: Aproximación de raíz cuadrada con el método de Newton."""

import math

def raiz_newton(x: float, tol: float = 1e-10) -> float:
    """Calcula la raíz cuadrada de x usando el método de Newton."""
    if x == 0:
        return 0.0
    g = x / 2.0
    while abs(g * g - x) > tol:
        g = (g + x / g) / 2.0
    return g

if __name__ == '__main__':
    assert abs(raiz_newton(25) - 5.0) < 1e-9
    assert abs(raiz_newton(2) - math.sqrt(2)) < 1e-9
    assert raiz_newton(0) == 0.0
    print('Todas las pruebas pasan')
