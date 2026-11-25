"""Pruebas de friccion. Ejecutar: python test_friccion.py"""
import math

from friccion import (
    aceleracion_horizontal,
    aceleracion_maxima_sin_deslizar,
    aceleracion_plano,
    distancia_frenado,
    friccion_cinetica,
    friccion_estatica_max,
    se_desliza,
)


def test_piso_horizontal() -> None:
    assert math.isclose(friccion_estatica_max(10.0, 0.5), 49.05)
    assert math.isclose(friccion_cinetica(10.0, 0.4), 39.24)
    # 40 N no vence los 49.05 N de fricción estática: no se mueve.
    assert aceleracion_horizontal(40.0, 10.0, 0.5, 0.4) == 0.0
    assert math.isclose(aceleracion_horizontal(60.0, 10.0, 0.5, 0.4), 2.076)


def test_plano_inclinado() -> None:
    assert se_desliza(30.0, 0.6) is False
    assert se_desliza(35.0, 0.6) is True
    assert math.isclose(aceleracion_plano(35.0, 0.3), 3.216, abs_tol=1e-3)
    assert aceleracion_plano(10.0, 0.5) == 0.0
    # Sin fricción, a 90° sería caída libre; a 30° es g/2.
    assert math.isclose(aceleracion_plano(30.0, 0.0), 4.905)


def test_robot() -> None:
    assert math.isclose(aceleracion_maxima_sin_deslizar(0.3), 2.943)
    assert math.isclose(distancia_frenado(1.5, 0.3), 0.3823, abs_tol=1e-4)
    assert distancia_frenado(0.0, 0.3) == 0.0


def test_entradas_invalidas() -> None:
    casos = [
        lambda: friccion_estatica_max(0.0, 0.5),
        lambda: friccion_cinetica(5.0, -0.1),
        lambda: se_desliza(90.0, 0.5),
        lambda: aceleracion_plano(-5.0, 0.2),
        lambda: distancia_frenado(1.0, 0.0),
    ]
    for caso in casos:
        try:
            caso()
        except ValueError:
            continue
        raise AssertionError("debió lanzar ValueError")


if __name__ == "__main__":
    test_piso_horizontal()
    test_plano_inclinado()
    test_robot()
    test_entradas_invalidas()
    print("OK: 4 pruebas de friccion")
