"""py4e cap. 7 · abrir un archivo, recorrerlo línea por línea y contar."""


def contar_lineas(ruta: str) -> int:
    """Devuelve cuántas líneas tiene el archivo de texto en `ruta`.

    Recorre el archivo con `for linea in archivo` (no uses read() ni
    readlines()): el objetivo es leer en streaming, una línea a la vez).
    Si el archivo no existe, deja que se propague FileNotFoundError.
    """
    contador = 0
    with open(ruta, "r", encoding="utf-8") as archivo:
        for _ in archivo:
            contador += 1
    return contador


def leer_en_mayusculas(ruta: str) -> list[str]:
    """Devuelve las líneas del archivo en mayúsculas y sin el salto de línea final.

    Ejercicio 1 del capítulo 7: cada línea termina en '\\n'; quítalo con rstrip().
    """
    resultado = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            resultado.append(linea.rstrip("\r\n").upper())
    return resultado


if __name__ == "__main__":
    nombre = input("Archivo: ")
    try:
        print(f"Líneas: {contar_lineas(nombre)}")
    except FileNotFoundError:
        print(f"No existe el archivo: {nombre}")
