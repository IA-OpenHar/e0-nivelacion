"""Pruebas del módulo proyectil. Ejecutar: python test_proyectil.py"""
import math

from proyectil import alcance, alcance_euler, altura_maxima, componentes, tiempo_vuelo


def test_componentes() -> None:
    vx, vy = componentes(15.0, 37.0)
    assert math.isclose(vx, 11.98, abs_tol=0.01)
    assert math.isclose(vy, 9.03, abs_tol=0.01)


def test_lanzamiento_45_grados() -> None:
    assert math.isclose(tiempo_vuelo(20.0, 45.0), 2.883, abs_tol=1e-3)
    assert math.isclose(alcance(20.0, 45.0), 40.775, abs_tol=1e-3)
    assert math.isclose(altura_maxima(20.0, 45.0), 10.194, abs_tol=1e-3)


def test_angulos_complementarios() -> None:
    # 30° y 60° dan el mismo alcance cuando se lanza y cae a la misma altura.
    assert math.isclose(alcance(20.0, 30.0), alcance(20.0, 60.0), rel_tol=1e-9)
    assert altura_maxima(20.0, 60.0) > altura_maxima(20.0, 30.0)


def test_lanzamiento_horizontal_desde_4_m() -> None:
    assert math.isclose(tiempo_vuelo(1.5, 0.0, h0=4.0), 0.903, abs_tol=1e-3)
    assert math.isclose(alcance(1.5, 0.0, h0=4.0), 1.355, abs_tol=1e-3)
    assert math.isclose(altura_maxima(1.5, 0.0, h0=4.0), 4.0)


def test_euler_contra_analitico() -> None:
    # Con dt = 1 ms el error del integrador debe quedar bajo 5 cm.
    assert abs(alcance_euler(20.0, 45.0, dt=0.001) - alcance(20.0, 45.0)) < 0.05


def test_entradas_invalidas() -> None:
    malas = [(-1.0, 45.0, 0.0), (20.0, 95.0, 0.0), (20.0, -5.0, 0.0), (20.0, 45.0, -1.0)]
    for v0, ang, h0 in malas:
        try:
            alcance(v0, ang, h0=h0)
        except ValueError:
            continue
        raise AssertionError(f"debió lanzar ValueError con {(v0, ang, h0)}")


if __name__ == "__main__":
    test_componentes()
    test_lanzamiento_45_grados()
    test_angulos_complementarios()
    test_lanzamiento_horizontal_desde_4_m()
    test_euler_contra_analitico()
    test_entradas_invalidas()
    print("OK: 6 pruebas de proyectil")
