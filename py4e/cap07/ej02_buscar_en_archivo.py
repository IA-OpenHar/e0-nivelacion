"""py4e cap. 7 · filtrar líneas de un archivo y promediar un campo."""

PREFIJO_CONFIANZA = "X-DSPAM-Confidence:"


def lineas_que_empiezan(ruta: str, prefijo: str) -> list[str]:
    """Devuelve, sin el salto final, las líneas que empiezan con `prefijo`.

    Usa str.startswith. El orden de salida es el del archivo.
    """
    encontradas = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if linea.startswith(prefijo):
                encontradas.append(linea.rstrip("\r\n"))
    return encontradas


def promedio_confianza(ruta: str) -> float:
    """Promedio de los números de las líneas que empiezan con PREFIJO_CONFIANZA.

    Ejercicio 2 del capítulo 7. El número va después de ':' (reutiliza la idea
    de ej02_extraer_confianza del Día 6). Lanza ValueError si no hay ninguna
    línea con ese prefijo: un promedio de cero elementos no existe.
    """
    valores = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if linea.startswith(PREFIJO_CONFIANZA):
                _, texto_numero = linea.split(":", 1)
                valores.append(float(texto_numero.strip()))

    if not valores:
        raise ValueError(f"No se encontraron líneas con el prefijo {PREFIJO_CONFIANZA}")

    return sum(valores) / len(valores)

if __name__ == "__main__":
    archivo_datos = "datos/mbox-short.txt"
    print(f"Líneas 'From ': {len(lineas_que_empiezan(archivo_datos, 'From '))}")
    print(f"Promedio de confianza: {promedio_confianza(archivo_datos)}")
