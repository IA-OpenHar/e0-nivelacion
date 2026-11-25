"""Pruebas de las prácticas p01–p05. Ejecutar: python test_practica.py"""
from p01_palabras_unicas import palabras_unicas
from p02_invertir_palabras import invertir_palabras
from p03_contar_vocales import contar_vocales
from p04_rotar_lista import rotar
from p05_fusionar_listas import fusionar_ordenadas


def test_p01() -> None:
    assert palabras_unicas("el gato y El perro y el loro") == [
        "el", "gato", "loro", "perro", "y"]
    assert palabras_unicas("") == []


def test_p02() -> None:
    assert invertir_palabras("hola mundo cruel") == "cruel mundo hola"
    assert invertir_palabras("  uno   dos ") == "dos uno"
    assert invertir_palabras("") == ""


def test_p03() -> None:
    assert contar_vocales("Murciélago") == 5
    assert contar_vocales("PINGÜINO") == 4
    assert contar_vocales("rtx 4090") == 0


def test_p04() -> None:
    original = [1, 2, 3, 4, 5]
    assert rotar(original, 2) == [4, 5, 1, 2, 3]
    assert rotar(original, 7) == [4, 5, 1, 2, 3]
    assert rotar(original, -1) == [2, 3, 4, 5, 1]
    assert original == [1, 2, 3, 4, 5]
    assert rotar([], 3) == []


def test_p05() -> None:
    assert fusionar_ordenadas([1, 4, 9], [2, 3, 10, 11]) == [
        1, 2, 3, 4, 9, 10, 11]
    assert fusionar_ordenadas([], [5]) == [5]
    assert fusionar_ordenadas([2, 2], [2]) == [2, 2, 2]


if __name__ == "__main__":
    test_p01()
    test_p02()
    test_p03()
    test_p04()
    test_p05()
    print("OK: 5 pruebas de las prácticas p01–p05")
