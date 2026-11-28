"""Pruebas de energia. Ejecutar: python3 test_energia.py"""

import math

from energia import (
    autonomia_horas,
    energia_cinetica,
    energia_potencial,
    potencia,
    trabajo,
    velocidad_tras_caida,
)


def test_trabajo() -> None:
    assert math.isclose(trabajo(50, 4), 200.0)
    assert math.isclose(trabajo(50, 4, 30), 173.205, abs_tol=1e-3)
    # Fuerza perpendicular al movimiento: no hace trabajo.
    assert math.isclose(trabajo(50, 4, 90), 0.0, abs_tol=1e-9)


def test_energias() -> None:
    assert math.isclose(energia_cinetica(2, 3), 9.0)
    # Doble de rapidez, cuatro veces la energía.
    assert math.isclose(energia_cinetica(2, 6), 4 * energia_cinetica(2, 3))
    assert math.isclose(energia_potencial(2, 5), 98.1)
    assert math.isclose(velocidad_tras_caida(5), 9.9045, abs_tol=1e-4)
    assert velocidad_tras_caida(0) == 0.0


def test_potencia_y_autonomia() -> None:
    w = energia_potencial(60, 1.5)
    assert math.isclose(potencia(w, 3), 294.3)
    assert math.isclose(autonomia_horas(2.3, 460), 5.0)


def test_entradas_invalidas() -> None:
    casos = [
        lambda: trabajo(10, -1),
        lambda: energia_cinetica(0, 3),
        lambda: energia_potencial(-2, 5),
        lambda: velocidad_tras_caida(-1),
        lambda: potencia(100, 0),
        lambda: autonomia_horas(2.3, 0),
    ]
    for caso in casos:
        try:
            caso()
        except ValueError:
            continue
        raise AssertionError("Debió lanzar ValueError")


if __name__ == "__main__":
    test_trabajo()
    test_energias()
    test_potencia_y_autonomia()
    test_entradas_invalidas()
    print("OK: 4 pruebas de energia")
