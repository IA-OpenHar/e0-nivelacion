"""Ejercicio 3: Contar números pares en un rango inclusivo."""
def contar_pares(a: int, b: int) -> int:
    """Devuelve cuántos pares hay entre a y b, ambos incluidos."""
    conteo = 0
    for num in range(a, b + 1):
        if num % 2 == 0:
            conteo += 1
    return conteo


if __name__ == '__main__':
    assert contar_pares(1, 10) == 5
    assert contar_pares(2, 2) == 1
    assert contar_pares(3, 3) == 0
    print('Todas las pruebas pasan')
