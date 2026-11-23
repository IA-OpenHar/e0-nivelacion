"""py4e cap. 6, ejercicios 3: contar una letra recorriendo la cadena."""


def contar_letra(texto: str, letra: str) -> int:
    """Devuelve cuantas veces aparece 'letra' en 'texto'.
    
    Recorre la cadena con un bucle 'for' (no uses str,count': el objetivo es practicar el recorrido). Distingue mayúculas de las minúscula.
    
    Lanza 'ValueError' si 'letra' no tiene exactamente 1 caracter.
    """
    if len(letra) != 1:
        raise ValueError("'letra' debe tener exactamente 1 caracter.")    
    contador = 0
    for caracter in texto:
        if caracter == letra:
            contador += 1
    return contador


if __name__ == "__main__":
    palabra = input("Palabra: ")
    objetivo = input('Letra: ')
    print(f"'{objetivo}' aparece {contar_letra(palabra, objetivo)} veces en '{palabra}'")