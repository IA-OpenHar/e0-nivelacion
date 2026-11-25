"""Pruebas de ej02_minimo_maximo.

Ejecutar: python test_ej02_minimo_maximo.py
"""
from ej02_minimo_maximo import minimo_maximo, procesar_entradas


def test_procesar_entradas() -> None:
    assert procesar_entradas(["4", "x", "-2.5", "done", "100"]) == [4.0, -2.5]
    assert procesar_entradas(["done"]) == []
    # Sin 'done' se procesa todo lo que llegó.
    assert procesar_entradas(["1", "2"]) == [1.0, 2.0]


def test_minimo_maximo() -> None:
    assert minimo_maximo([4.0, -2.5, 9.0, 0.0]) == (-2.5, 9.0)
    assert minimo_maximo([7.0]) == (7.0, 7.0)


def test_lista_vacia() -> None:
    try:
        minimo_maximo([])
    except ValueError:
        return
    raise AssertionError("debió lanzar ValueError")


if __name__ == "__main__":
    test_procesar_entradas()
    test_minimo_maximo()
    test_lista_vacia()
    print("OK: 3 pruebas de ej02_minimo_maximo")
