"""Pruebas de newton. Ejecutar: python test_newton.py"""
import math

from newton import (aceleracion, fuerza_neta, libras_a_kg, normal_ascensor, peso,
                    suma_fuerzas)
def test_segunda_ley() -> None:
    assert math.isclose(aceleracion(10.0, 2.0), 5.0)
    assert math.isclose(fuerza_neta(1200.0, 2.5), 3000.0)
    # F = m·a y a = F/m son inversas: ida y vuelta devuelve el valor original.
    assert math.isclose(aceleracion(fuerza_neta(3.0, 4.0), 3.0), 4.0)
def test_peso_y_ascensor() -> None:
    assert math.isclose(peso(10.0), 98.1)
    assert math.isclose(normal_ascensor(70.0, 1.5), 791.7)
    assert math.isclose(normal_ascensor(70.0, 0.0), peso(70.0))
    # Caída libre: el piso deja de empujar.
    assert math.isclose(normal_ascensor(70.0, -9.81), 0.0, abs_tol=1e-9)
def test_vectores() -> None:
    fx, fy = suma_fuerzas([(30.0, 0.0), (0.0, 40.0)])
    assert math.isclose(math.hypot(fx, fy), 50.0)
    assert suma_fuerzas([]) == (0.0, 0.0)
    assert suma_fuerzas([(5.0, -2.0), (-5.0, 2.0)]) == (0.0, 0.0)
def test_libras() -> None:
    assert math.isclose(libras_a_kg(154.0), 69.853, abs_tol=1e-3)
    assert math.isclose(libras_a_kg(66.0), 29.937, abs_tol=1e-3)
def test_entradas_invalidas() -> None:
    casos = [lambda: aceleracion(10.0, 0.0), lambda: fuerza_neta(-1.0, 2.0),
            lambda: peso(0.0), lambda: normal_ascensor(70.0, -12.0)]
    for caso in casos:
        try:
            caso()
        except ValueError:
            continue
        raise AssertionError("debió lanzar ValueError")

if __name__ == "__main__":
    test_segunda_ley()
    test_peso_y_ascensor()
    test_vectores()
    test_libras()
    test_entradas_invalidas()
    print("OK: 5 pruebas de newton")
