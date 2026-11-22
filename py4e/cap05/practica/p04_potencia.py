"""Ejercicio 4: Calcular potencia usando un bucle sin el operador **."""
def potencia(base: float, exponente: int) -> float:
    """Calcula base elevado a exponente con un bucle, exponente >= 0."""
    resultado = 1.0
    for _ in range(exponente):
        resultado *= base
    return resultado


if __name__ == '__main__':
    assert potencia(2, 10) == 1024
    assert potencia(5, 0) == 1
    assert potencia(1.5, 2) == 2.25
    print('Todas las pruebas pasan')
