"""Pruebas de ej01_contar_palabras.

Ejecutar: python test_ej01_contar_palabras.py
"""

import os
import tempfile

from ej01_contar_palabras import (
    contar_palabras,
    contar_palabras_archivo,
    palabra_mas_frecuente,
)


def test_contar_palabras() -> None:
    conteo = contar_palabras("Hola hola, mundo. ¡HOLA!")
    assert conteo == {"hola": 3, "mundo": 1}
    assert contar_palabras("") == {}
    # Un signo suelto no es una palabra.
    assert contar_palabras("sí, no") == {"sí": 1, "no": 1}


def test_contar_palabras_archivo() -> None:
    with tempfile.NamedTemporaryFile(
        "w", suffix=".txt", delete=False, encoding="utf-8"
    ) as f:
        f.write("uno dos\ndos tres tres tres\n")
        ruta = f.name
    try:
        assert contar_palabras_archivo(ruta) == {"uno": 1, "dos": 2, "tres": 3}
    finally:
        os.remove(ruta)


def test_palabra_mas_frecuente() -> None:
    assert palabra_mas_frecuente({"a": 1, "b": 4, "c": 2}) == ("b", 4)
    # Empate: gana el orden alfabético.
    assert palabra_mas_frecuente({"robot": 3, "humano": 3}) == ("humano", 3)


def test_vacio() -> None:
    try:
        palabra_mas_frecuente({})
    except ValueError:
        return
    raise AssertionError("Debió lanzar ValueError")


if __name__ == "__main__":
    test_contar_palabras()
    test_contar_palabras_archivo()
    test_palabra_mas_frecuente()
    test_vacio()
    print("OK: 4 pruebas de ej01_contar_palabras")
