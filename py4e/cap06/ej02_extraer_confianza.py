"""py4e cap. 6, ejercicio 5: extraer un número de una línea con find y slicing."""


def extraer_confianza(linea: str) -> float:
    """Devuelve como `float` lo que hay después del primer `:` de `linea`.

    Usa `str.find` y slicing (no uses `split`). Tolera espacios antes y después
    del número. Lanza `ValueError` si la línea no contiene `:`.
    """
    pos_dos_puntos = linea.find(":")
    if pos_dos_puntos == -1:
        raise ValueError("La línea no contiene ':'")

    subcadena = linea[pos_dos_puntos + 1:].strip()
    return float(subcadena)


if __name__ == "__main__":
    print(extraer_confianza("X-DSPAM-Confidence:0.8475"))