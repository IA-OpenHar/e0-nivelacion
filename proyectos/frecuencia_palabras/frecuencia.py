"""Mini-proyecto de la semana 2: frecuencia de palabras en un archivo.

Uso: python frecuencia.py datos/ejemplo.txt 5
"""
import sys

SIGNOS = ".,;:!?¡¿\\\"'()«»"
N_POR_DEFECTO = 10


def normalizar(texto: str) -> list[str]:
    """Devuelve las palabras de `texto` en minúsculas y sin signos.

    Separa con split() y quita de los bordes de cada palabra los
    caracteres de SIGNOS. Descarta las que quedan vacías. Mantiene
    el orden y las repeticiones.
    """
    palabras = []
    for trozo in texto.split():
        limpia = trozo.strip(SIGNOS).lower()
        if limpia:
            palabras.append(limpia)
    return palabras


def contar(palabras: list[str]) -> dict[str, int]:
    """Cuenta cuántas veces aparece cada palabra (palabra -> cantidad)."""
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo


def top_n(conteo: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Devuelve los `n` pares (palabra, cantidad) más frecuentes.

    Orden: cantidad de mayor a menor; si empatan, palabra en orden
    alfabético. Si hay menos de `n` palabras, devuelve todas.
    ValueError si n < 1.
    """
    if n < 1:
        raise ValueError("n debe ser al menos 1")
    ordenados = sorted(conteo.items(), key=lambda par: (-par[1], par[0]))
    return ordenados[:n]


def formatear(pares: list[tuple[str, int]], total: int) -> str:
    """Arma la tabla de texto, una línea por par, sin salto final.

    Formato de cada línea (posición desde 1, palabra en 15 columnas,
    cantidad en 4 y porcentaje del total con 1 decimal en 5):
      f"{i:>2}. {palabra:<15}{n:>4} {porcentaje:5.1f} %"
    Lista vacía -> "". ValueError si total < 1.
    """
    if total < 1:
        raise ValueError("total debe ser al menos 1")
    if not pares:
        return ""
    lineas = []
    for i, (palabra, n) in enumerate(pares, start=1):
        porcentaje = (n / total) * 100
        lineas.append(f"{i:>2}. {palabra:<15}{n:>4} {porcentaje:5.1f} %")
    return "\n".join(lineas)


def leer_archivo(ruta: str) -> str:
    """Devuelve el contenido del archivo en `ruta` (utf-8)."""
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()


def main(argv: list[str]) -> int:
    """Programa completo. `argv` son los argumentos sin el nombre.

    - 0 o más de 2 argumentos: imprime el uso en stderr y devuelve 2.
    - N no entero, o N < 1: mensaje en stderr y devuelve 2.
    - Archivo inexistente: mensaje en stderr y devuelve 1.
    - Archivo sin palabras: imprime "El archivo no tiene palabras", 0.
    - Si todo va bien: imprime la tabla del top N (N_POR_DEFECTO si
      no se pasa), luego "Total: X palabras, Y distintas", y
      devuelve 0.
    """
    if len(argv) == 0 or len(argv) > 2:
        print("Uso: python frecuencia.py ARCHIVO [N]", file=sys.stderr)
        return 2

    ruta = argv[0]
    try:
        n = int(argv[1]) if len(argv) == 2 else N_POR_DEFECTO
        texto = leer_archivo(ruta)
        palabras = normalizar(texto)
        if not palabras:
            print("El archivo no tiene palabras")
            return 0
        conteo = contar(palabras)
        mejores = top_n(conteo, n)
        print(formatear(mejores, len(palabras)))
        print(f"Total: {len(palabras)} palabras, {len(conteo)} distintas")
        return 0
    except ValueError:
        print(
            "Error: N debe ser un número entero mayor o igual a 1.",
            file=sys.stderr,
        )
        return 2

    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{ruta}'.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    # El código de salida le dice a la terminal (y a la CI) si falló.
    sys.exit(main(sys.argv[1:]))
