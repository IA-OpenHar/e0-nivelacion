"""py4e cap. 8 · listas: modificar en el sitio vs. devolver una lista nueva."""


def chop(t: list) -> None:
    """Quita el primer y el último elemento de `t` EN EL SITIO y devuelve None.

    Ejercicio 1 del capítulo 8. Modifica la lista que recibe (no crea otra).
    Lanza ValueError (mensaje en español) si `t` tiene menos de 2 elementos.
    """
    if len(t) < 2:
        raise ValueError("La lista debe tener al menos 2 elementos.")
    del t[0]
    del t[-1]


def middle(t: list) -> list:
    """Devuelve una lista NUEVA sin el primer ni el último elemento de `t`.

    La lista original no cambia. Con menos de 2 elementos devuelve [].
    """
    return t[1:-1]


def promedio(numeros: list[float]) -> float:
    """Promedio de una lista de números.

    Lanza ValueError si la lista está vacía; un promedio de cero
    elementos no existe.
    """
    if not numeros:
        raise ValueError("No se puede calcular el promedio de una lista vacía.")
    return sum(numeros) / len(numeros)


if __name__ == "__main__":
    datos = [3, 1, 4, 1, 5, 9]
    print(f"middle({datos}) = {middle(datos)}; original: {datos}")
    chop(datos)
    print(f"después de chop: {datos}")
    print(f"promedio: {promedio(datos):.2f}")
