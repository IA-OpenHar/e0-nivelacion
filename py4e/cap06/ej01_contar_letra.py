"""py4e cap. 6, ejercicio 3: contar una letra recorriendo la cadena."""

def contar_letra(texto: str, letra: str) -> int:
    """Devuelve cuántas veces aparece 'letra' en 'texto'.

    Recorre la cadena con un bucle 'for' (no uses str.count: el objetivo es
    practicar el recorrido y distinguir las mayúsculas de las minúsculas).

    Lanza 'ValueError' si 'letra' no tiene exactamente 1 carácter.
    """
    if len(letra) != 1:
        raise ValueError("'letra' debe tener exactamente 1 carácter.")
    contador = 0
    for caracter in texto:
        if caracter == letra:
            contador += 1
    return contador


if __name__ == "__main__":
    palabra = input("Palabra: ")
    objetivo = input("Letra: ")
    print(f"'{objetivo}' aparece {contar_letra(palabra, objetivo)} veces en '{palabra}'")
