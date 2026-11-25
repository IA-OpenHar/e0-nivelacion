"""B3 · práctica 2: invertir el orden de las palabras de una frase."""


def invertir_palabras(frase: str) -> str:
    """Devuelve las palabras de `frase` en orden inverso, con un espacio.

    Los espacios repetidos o al borde no cuentan como palabras.
    """
    return " ".join(frase.split()[::-1])


if __name__ == "__main__":
    print(invertir_palabras("primero se mide después se optimiza"))
