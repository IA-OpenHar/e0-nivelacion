"""Pruebas de dinamica_problemas.

Ejecutar: python test_dinamica_problemas.py
"""
import math

from dinamica_problemas import (
    aceleracion_atwood,
    aceleracion_mesa_polea,
    potencia_subida,
    rapidez_final_plano,
    tension_atwood,
    tension_mesa_polea,
)


def test_atwood() -> None:
    assert math.isclose(aceleracion_atwood(5, 3), 2.4525)
    assert math.isclose(tension_atwood(5, 3), 36.7875)
    # Masas iguales: equilibrio, y la tensión es el peso de una.
    assert math.isclose(aceleracion_atwood(4, 4), 0.0, abs_tol=1e-12)
    assert math.isclose(tension_atwood(4, 4), 4 * 9.81)
    # Si sube m1, la aceleración sale negativa.
    assert aceleracion_atwood(3, 5) < 0


def test_mesa_polea() -> None:
    assert math.isclose(aceleracion_mesa_polea(4, 2, 0.2), 1.962)
    assert math.isclose(tension_mesa_polea(4, 2, 0.2), 15.696)
    # Fricción grande: no arranca y la cuerda sostiene todo el peso.
    assert aceleracion_mesa_polea(4, 2, 0.6) == 0.0
    assert math.isclose(tension_mesa_polea(4, 2, 0.6), 2 * 9.81)


def test_plano_y_potencia() -> None:
    assert math.isclose(
        rapidez_final_plano(2, 30, 0.2), 5.0643, abs_tol=1e-4
    )
    assert math.isclose(
        rapidez_final_plano(2, 30, 0.0), math.sqrt(2 * 9.81 * 2)
    )
    assert rapidez_final_plano(2, 10, 0.5) == 0.0
    assert math.isclose(potencia_subida(60, 3, 6), 294.3)


def test_entradas_invalidas() -> None:
    casos = [
        lambda: aceleracion_atwood(0, 3),
        lambda: tension_atwood(5, -1),
        lambda: aceleracion_mesa_polea(4, 2, -0.1),
        lambda: rapidez_final_plano(2, 90, 0.2),
        lambda: rapidez_final_plano(-1, 30, 0.2),
        lambda: potencia_subida(60, 3, 0),
    ]
    for caso in casos:
        try:
            caso()
        except ValueError:
            continue
        raise AssertionError("Debió lanzar ValueError")


if __name__ == "__main__":
    test_atwood()
    test_mesa_polea()
    test_plano_y_potencia()
    test_entradas_invalidas()
    print("OK: 4 pruebas de dinamica_problemas")
