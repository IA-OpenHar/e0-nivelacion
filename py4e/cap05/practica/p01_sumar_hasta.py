"""Ejercicio 1: Sumar de 1 hasta n."""
def sumar_hasta(n: int) -> int:
    """Devuelve 1 + 2 + ... + n. Si n <= 0, devuelve 0."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


if __name__ == '__main__':
    assert sumar_hasta(10) == 55
    assert sumar_hasta(1) == 1
    assert sumar_hasta(0) == 0
    assert sumar_hasta(-5) == 0
    print('Todas las pruebas pasan')
