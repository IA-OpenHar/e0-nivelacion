"""Ejercicio 7: Contar los dígitos de un entero sin convertir a texto."""
def contar_digitos(n: int) -> int:
    """Cuenta cuántos dígitos tiene n usando while y // 10."""
    if n == 0:
        return 1
    n = abs(n)
    digitos = 0
    while n > 0:
        n //= 10
        digitos += 1
    return digitos

if __name__ == '__main__':
    assert contar_digitos(12345) == 5
    assert contar_digitos(7) == 1
    assert contar_digitos(0) == 1
    print('Todas las pruebas pasan')
