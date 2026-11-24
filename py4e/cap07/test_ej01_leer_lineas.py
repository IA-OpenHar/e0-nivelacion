"""Pruebas de ej01_leer_lineas. Ejecutar: python test_ej01_leer_lineas.py"""
import os
import tempfile

from ej01_leer_lineas import contar_lineas, leer_en_mayusculas
def _crear(carpeta: str, nombre: str, texto: str) -> str:
    # Archivo temporal propio: la prueba no depende de datos externos.
    ruta = os.path.join(carpeta, nombre)
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write(texto)
    return ruta
def test_contar_lineas() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        assert contar_lineas(_crear(tmp, "tres.txt", "uno\ndos\ntres\n")) == 3
        # Sin salto de línea al final también cuenta como línea.
        assert contar_lineas(_crear(tmp, "sin_fin.txt", "a\nb")) == 2
        assert contar_lineas(_crear(tmp, "vacio.txt", "")) == 0
def test_mayusculas() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        ruta = _crear(tmp, "texto.txt", "hola mundo\nñandú veloz\n")
        assert leer_en_mayusculas(ruta) == ["HOLA MUNDO", "ÑANDÚ VELOZ"]
def test_archivo_inexistente() -> None:
    try:
        contar_lineas("no_existe_este_archivo.txt")
    except FileNotFoundError:
        return
    raise AssertionError("debió lanzar FileNotFoundError")

if __name__ == "__main__":
    test_contar_lineas()
    test_mayusculas()
    test_archivo_inexistente()
    print("OK: 3 pruebas de ej01_leer_lineas")
