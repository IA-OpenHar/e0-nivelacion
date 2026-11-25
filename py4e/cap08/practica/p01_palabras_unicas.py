"""B3 · práctica 1: palabras únicas de un texto (py4e cap. 8, ejercicio 4)."""


def palabras_unicas(texto: str) -> list[str]:
    """Palabras distintas de `texto`, en minúsculas y en orden alfabético.

    Separa con split(); no hace falta quitar signos de puntuación.
    """
    return sorted(set(texto.lower().split()))


if __name__ == "__main__":
    print(palabras_unicas("But soft what light through yonder window breaks"))
