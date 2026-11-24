"""Pruebas de bytes vs. caracteres. Ejecutar: python test_ej03_bytes_vs_caracteres.py"""
import math

from ej03_bytes_vs_caracteres import contar_bytes_utf8, razon_bytes_por_caracter


def test_ascii() -> None:
    assert contar_bytes_utf8("hola") == 4
    assert math.isclose(razon_bytes_por_caracter("IA"), 1.0)


def test_espanol_y_emoji() -> None:
    # ñ y ú ocupan 2 bytes cada una en UTF-8; el emoji ocupa 4.
    assert contar_bytes_utf8("ñandú") == 7
    assert math.isclose(razon_bytes_por_caracter("ñandú"), 1.4)
    assert contar_bytes_utf8("🤖") == 4


def test_texto_vacio() -> None:
    assert contar_bytes_utf8("") == 0
    try:
        razon_bytes_por_caracter("")
    except ValueError:
        return
    raise AssertionError("debió lanzar ValueError: no hay caracteres")


if __name__ == "__main__":
    test_ascii()
    test_espanol_y_emoji()
    test_texto_vacio()
    print("OK: 3 pruebas de bytes vs. caracteres")
