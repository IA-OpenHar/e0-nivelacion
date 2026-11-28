"""Pruebas de frecuencia. Ejecutar: python test_frecuencia.py"""
import contextlib
import io
import os
import tempfile

from frecuencia import contar, formatear, main, normalizar, top_n


def _correr(argv: list[str]) -> tuple[int, str, str]:
    # Captura lo que main imprime para probar la salida sin mirarla.
    salida, errores = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(salida), \
            contextlib.redirect_stderr(errores):
        codigo = main(argv)
    return codigo, salida.getvalue(), errores.getvalue()


def test_normalizar_y_contar() -> None:
    palabras = normalizar("¡Hola, robot! El robot dice: «hola».")
    assert palabras == ["hola", "robot", "el", "robot", "dice", "hola"]
    assert normalizar("  ¿?  ") == []
    assert contar(palabras) == {"hola": 2, "robot": 2, "el": 1, "dice": 1}


def test_top_n() -> None:
    conteo = {"el": 3, "robot": 2, "aprende": 2, "dato": 1}
    # Empate en 2: gana el orden alfabético.
    assert top_n(conteo, 3) == [("el", 3), ("aprende", 2), ("robot", 2)]
    assert len(top_n(conteo, 50)) == 4
    try:
        top_n(conteo, 0)
    except ValueError:
        pass
    else:
        raise AssertionError("Debió lanzar ValueError")


def test_formatear() -> None:
    tabla = formatear([("robot", 3), ("el", 1)], 12)
    assert tabla.split("\n") == [
        " 1. robot             3  25.0 %",
        " 2. el                1   8.3 %",
    ]
    assert formatear([], 5) == ""


def test_main() -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False,
                                     encoding="utf-8") as f:
        f.write("uno dos dos\ntres tres tres\n")
        ruta = f.name
    try:
        codigo, salida, _ = _correr([ruta, "2"])
        assert codigo == 0
        assert salida.split("\n")[0].startswith(" 1. tres")
        assert "Total: 6 palabras, 3 distintas" in salida
        assert _correr([ruta, "dos"])[0] == 2
        assert _correr([ruta, "0"])[0] == 2
    finally:
        os.remove(ruta)
    assert _correr([])[0] == 2
    assert _correr(["no_existe_este_archivo.txt"])[0] == 1


if __name__ == "__main__":
    test_normalizar_y_contar()
    test_top_n()
    test_formatear()
    test_main()
    print("OK: 4 pruebas de frecuencia")
