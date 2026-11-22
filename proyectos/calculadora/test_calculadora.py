import math

from calculadora import calcular, formatear, interpretar


def debe_fallar(funcion, excepcion, *args) -> None:
    """Verifica que funcion(*args) lance la excepción indicada."""
    try:
        funcion(*args)
    except excepcion:
        return
    mensaje = f"{funcion.__name__}{args} debió lanzar {excepcion.__name__}"
    raise AssertionError(mensaje)


if __name__ == '__main__':
    assert calcular(3, '+', 4) == 7
    assert calcular(10, '-', 2.5) == 7.5
    assert calcular(6, '*', 7) == 42
    assert calcular(7, '/', 2) == 3.5
    assert calcular(2, '**', 10) == 1024
    # 0.1 + 0.2 da 0.30000000000000004: los float se comparan con tolerancia
    assert math.isclose(calcular(0.1, '+', 0.2), 0.3)
    debe_fallar(calcular, ZeroDivisionError, 7, '/', 0)
    debe_fallar(calcular, ValueError, 2, '^', 3)
    debe_fallar(calcular, ValueError, -8, '**', 1 / 3)
    debe_fallar(calcular, OverflowError, 10.0, '**', 400.0)
    assert interpretar('3 + 4') == (3.0, '+', 4.0)
    assert interpretar('  2.5   *  -1 ') == (2.5, '*', -1.0)
    # Pruebas de los retos opcionales (sin espacios y sin nan/inf)
    assert interpretar('3+4') == (3.0, '+', 4.0)
    assert interpretar('-2.5*4') == (-2.5, '*', 4.0)
    debe_fallar(interpretar, ValueError, 'nan + 5')
    debe_fallar(interpretar, ValueError, 'inf * 2')
    debe_fallar(interpretar, ValueError, 'tres + 4')
    assert formatear(7.0) == '7'
    assert formatear(3.5) == '3.5'
    assert formatear(-2.0) == '-2'
    print('Todas las pruebas pasan')
