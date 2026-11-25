"""B3 · práctica 5: fusionar dos listas ya ordenadas (base del merge sort)."""


def fusionar_ordenadas(a: list[int], b: list[int]) -> list[int]:
    """Une dos listas ordenadas en una lista ordenada nueva.

    Sin sort() ni sorted(): avanza con dos índices, uno por lista, y en cada
    paso toma el menor. Así el costo es proporcional a len(a) + len(b).
    """
    resultado: list[int] = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1

    resultado.extend(a[i:])
    resultado.extend(b[j:])
    return resultado


if __name__ == "__main__":
    print(fusionar_ordenadas([1, 4, 9], [2, 3, 10, 11]))
