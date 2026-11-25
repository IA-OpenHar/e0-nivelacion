"""B3 · práctica 4: rotar una lista k posiciones a la derecha."""


def rotar(lista: list, k: int) -> list:
    """Devuelve una lista NUEVA rotada k posiciones a la derecha.

    k puede ser mayor que la longitud (da vueltas) o negativo (rota a la
    izquierda). La lista original no cambia. Una lista vacía devuelve [].
    """
    if not lista:
        return []
    pasos = k % len(lista)
    if pasos == 0:
        return lista[:]
    return lista[-pasos:] + lista[:-pasos]


if __name__ == "__main__":
    print(rotar([1, 2, 3, 4, 5], 2))
