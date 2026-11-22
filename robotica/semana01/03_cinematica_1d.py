"""Funciones de cinemática en una dimensión (1D) para robótica móvil."""


def velocidad_media(x0, x1, t0, t1):
    """Calcula la velocidad media (m/s) entre dos instantes de tiempo."""
    if t1 == t0:
        raise ValueError('El tiempo transcurrido (t1 - t0) no puede ser cero.')
    return (x1 - x0) / (t1 - t0)


def posicion(x0, v0, a, t):
    """Calcula la posición final (m) bajo aceleración constante."""
    return x0 + (v0 * t) + (0.5 * a * (t ** 2))


def velocidad(v0, a, t):
    """Calcula la velocidad final (m/s) bajo aceleración constante."""
    return v0 + (a * t)


if __name__ == '__main__':
    # 1. Pruebas de la tabla de la guía
    assert velocidad_media(0, 3, 0, 2) == 1.5
    assert posicion(0, 2, 0.5, 4) == 12.0
    assert velocidad(2, 0.5, 4) == 4.0

    # 2. Prueba del Reto: verificar que t1 == t0 lance ValueError claro
    try:
        velocidad_media(0, 3, 2, 2)
    except ValueError as error:
        print(f'Reto verificado correctamente -> {error}')

    print('Todas las pruebas de cinemática 1D pasan')
