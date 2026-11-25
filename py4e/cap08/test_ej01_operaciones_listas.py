"""Pruebas de ej01_operaciones_listas.

Ejecutar: python test_ej01_operaciones_listas.py
"""
import math

from ej01_operaciones_listas import chop, middle, promedio


def test_chop_modifica_en_el_sitio() -> None:
    t = [1, 2, 3, 4]
    resultado = chop(t)
    # chop devuelve None: el cambio queda en la misma lista.
    assert resultado is None
    assert t == [2, 3]


def test_middle_no_toca_el_original() -> None:
    t = [1, 2, 3, 4]
    nueva = middle(t)
    assert nueva == [2, 3]
    assert t == [1, 2, 3, 4]
    assert nueva is not t
    assert middle([7]) == []


def test_promedio() -> None:
    assert math.isclose(promedio([1, 2, 3, 4]), 2.5)
    assert math.isclose(promedio([-1.5]), -1.5)


def test_errores() -> None:
    for caso in (lambda: chop([1]), lambda: promedio([])):
        try:
            caso()
        except ValueError:
            continue
        raise AssertionError("debió lanzar ValueError")


if __name__ == "__main__":
    test_chop_modifica_en_el_sitio()
    test_middle_no_toca_el_original()
    test_promedio()
    test_errores()
    print("OK: 4 pruebas de ej01_operaciones_listas")
