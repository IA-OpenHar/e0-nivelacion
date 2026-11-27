"""py4e cap. 9 · diccionarios: contar palabras de un texto o archivo."""

SIGNOS = ".,;:!?¿¡\"'()"


def contar_palabras(texto: str) -> dict[str, int]:
    """Cuenta cuántas veces aparece cada palabra en `texto`.

    Pasa todo a minúsculas, separa con split() y quita de los bordes
    de cada palabra los caracteres de SIGNOS. Las palabras que quedan
    vacías no se cuentan. Devuelve un diccionario palabra -> cantidad.
    """
    conteo: dict[str, int] = {}
    for palabra in texto.lower().split():
        limpia = palabra.strip(SIGNOS)
        if limpia:
            conteo[limpia] = conteo.get(limpia, 0) + 1
    return conteo


def contar_palabras_archivo(ruta: str) -> dict[str, int]:
    """Lee el archivo en `ruta` (utf-8) y cuenta sus palabras.

    Usa contar_palabras sobre el contenido completo del archivo.
    """
    with open(ruta, encoding="utf-8") as archivo:
        contenido = archivo.read()
    return contar_palabras(contenido)


def palabra_mas_frecuente(conteo: dict[str, int]) -> tuple[str, int]:
    """Devuelve (palabra, cantidad) de la palabra con más apariciones.

    Si hay empate, gana la que va primero en orden alfabético.
    Lanza ValueError si `conteo` está vacío. Hazlo con un bucle,
    sin max() ni sorted().
    """
    if not conteo:
        raise ValueError("El diccionario de conteo está vacío.")

    mejor_palabra = ""
    mejor_cantidad = -1

    for palabra, cantidad in conteo.items():
        if cantidad > mejor_cantidad or (
            cantidad == mejor_cantidad and palabra < mejor_palabra
        ):
            mejor_palabra = palabra
            mejor_cantidad = cantidad

    return (mejor_palabra, mejor_cantidad)


if __name__ == "__main__":
    frase = "El robot mide, el robot decide, el humano revisa."
    conteo = contar_palabras(frase)
    print(conteo)
    print("Más frecuente:", palabra_mas_frecuente(conteo))
