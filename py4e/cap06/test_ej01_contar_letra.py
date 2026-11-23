"""Pruebas de contar_letra. Ejecutar: python test_ej01_contar_letra.py"""
from ej01_contar_letra import contar_letra


def test_casos_normales() -> None:
    assert contar_letra("banana", "a") == 3
    assert contar_letra("banana", "n") == 2


def test_bordes() -> None:
    assert contar_letra("banana", "z") == 0
    assert contar_letra("", "a") == 0
    # Distingue mayúsculas: 'B' y 'b' son caracteres distintos.
    assert contar_letra("Banana", "b") == 0
    assert contar_letra("ñandú", "ñ") == 1


def test_letra_invalida() -> None:
    for mala in ("", "an"):
        try:
            contar_letra("banana", mala)
        except ValueError:
            continue
        raise AssertionError(f"debió lanzar ValueError con {mala!r}")


if __name__ == "__main__":
    test_casos_normales()
    test_bordes()
    test_letra_invalida()
    print("OK: 3 pruebas de contar_letra")