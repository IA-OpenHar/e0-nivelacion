"""py4e cap. 9 · ejercicios 3, 4 y 5: remitentes y dominios del correo."""

ARCHIVO = "../cap07/datos/mbox-short.txt"


def remitentes(lineas: list[str]) -> dict[str, int]:
    """Cuenta los mensajes de cada dirección de correo.

    Solo mira las líneas que empiezan con "From " (con espacio; las que
    empiezan con "From:" no cuentan). La dirección es la segunda
    palabra de esa línea. Devuelve dirección -> cantidad.
    """
    conteo: dict[str, int] = {}
    for linea in lineas:
        if linea.startswith("From "):
            palabras = linea.split()
            if len(palabras) >= 2:
                correo = palabras[1]
                conteo[correo] = conteo.get(correo, 0) + 1
    return conteo


def remitente_frecuente(conteo: dict[str, int]) -> tuple[str, int]:
    """Devuelve (dirección, cantidad) del remitente con más mensajes.

    Bucle de máximo, sin max(). Si hay empate, gana el primero que
    aparece en el diccionario. ValueError si `conteo` está vacío.
    """
    if not conteo:
        raise ValueError("El diccionario de remitentes está vacío.")

    mejor_correo = ""
    mejor_cantidad = -1

    for correo, cantidad in conteo.items():
        if cantidad > mejor_cantidad:
            mejor_correo = correo
            mejor_cantidad = cantidad

    return (mejor_correo, mejor_cantidad)


def dominios(conteo: dict[str, int]) -> dict[str, int]:
    """Agrupa un conteo por dirección en un conteo por dominio.

    El dominio es lo que va después de la "@". Las cantidades de
    direcciones del mismo dominio se suman.
    """
    conteo_dominios: dict[str, int] = {}
    for correo, cantidad in conteo.items():
        pos_arroba = correo.find("@")
        if pos_arroba != -1:
            dominio = correo[pos_arroba + 1:]
            conteo_dominios[dominio] = (
                conteo_dominios.get(dominio, 0) + cantidad
            )
    return conteo_dominios


if __name__ == "__main__":
    with open(ARCHIVO, encoding="utf-8") as f:
        conteo_correos = remitentes(f.readlines())
    print(
        len(conteo_correos),
        "direcciones,",
        sum(conteo_correos.values()),
        "mensajes",
    )
    print("Más frecuente:", remitente_frecuente(conteo_correos))
    print(dominios(conteo_correos))
