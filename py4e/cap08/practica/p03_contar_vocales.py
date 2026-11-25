"""B3 · práctica 3: contar vocales, incluidas las tildadas."""

VOCALES = "aeiouáéíóúü"


def contar_vocales(texto: str) -> int:
    """Cuántas vocales tiene `texto`, sin distinguir mayúsculas.

    Cuentan las letras de VOCALES (con tilde y diéresis incluidas).
    """
    return sum(1 for letra in texto.lower() if letra in VOCALES)


if __name__ == "__main__":
    print(contar_vocales("Murciélago"))
