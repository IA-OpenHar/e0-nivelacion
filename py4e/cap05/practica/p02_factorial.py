"""Ejercicio 2: Factorial de n usando un bucle."""
def factorial(n: int) -> int:
    """Devuelve n! con un bucle; 0! = 1."""
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


if __name__ == '__main__':
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    print('Todas las pruebas pasan')
