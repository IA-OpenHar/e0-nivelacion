"""Pruebas de extraer_confianza. Ejecutar: python test_ej02_extraer_confianza.py"""
import math

from ej02_extraer_confianza import extraer_confianza


def test_linea_py4e() -> None:
    assert math.isclose(extraer_confianza("X-DSPAM-Confidence:0.8475"), 0.8475)


def test_espacios() -> None:
    assert math.isclose(extraer_confianza("X-DSPAM-Confidence:  0.6178  "), 0.6178)


def test_sin_dos_puntos() -> None:
    try:
        extraer_confianza("X-DSPAM-Confidence 0.8475")
    except ValueError:
        return
    raise AssertionError("debió lanzar ValueError: la línea no tiene ':'")


if __name__ == "__main__":
    test_linea_py4e()
    test_espacios()
    test_sin_dos_puntos()
    print("OK: 3 pruebas de extraer_confianza")
