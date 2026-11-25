"""py4e cap. 8 · ejercicio 6: mínimo y máximo de números ingresados."""

FIN = "done"


def procesar_entradas(entradas: list[str]) -> list[float]:
    """Convierte las entradas a float hasta encontrar FIN ('done').

    Ignora las entradas que no son números (no se cae: usa try/except).
    Lo que viene después de FIN no se procesa.
    """
    numeros: list[float] = []
    for item in entradas:
        if item == FIN:
            break
        try:
            numeros.append(float(item))
        except ValueError:
            continue
    return numeros


def minimo_maximo(lista_numeros: list[float]) -> tuple[float, float]:
    """Devuelve (mínimo, máximo) recorriendo la lista una sola vez.

    No uses min() ni max(): el objetivo es el patrón del bucle.
    Lanza ValueError si la lista está vacía.
    """
    if not lista_numeros:
        raise ValueError("La lista no puede estar vacía.")

    minimo = lista_numeros[0]
    maximo = lista_numeros[0]

    for num in lista_numeros[1:]:
        if num < minimo:
            minimo = num
        if num > maximo:
            maximo = num

    return (minimo, maximo)


if __name__ == "__main__":
    entradas = []
    while True:
        texto = input("Número (o done): ")
        entradas.append(texto)
        if texto == FIN:
            break
    numeros = procesar_entradas(entradas)
    if numeros:
        menor, mayor = minimo_maximo(numeros)
        print(f"Mínimo: {menor} · Máximo: {mayor}")
    else:
        print("No ingresaste números válidos.")
