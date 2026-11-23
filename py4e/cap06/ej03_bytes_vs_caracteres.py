"""Frontera B2: un tokenizador byte-level ve bytes, no letras."""


def contar_bytes_utf8(texto: str) -> int:
    """Devuelve cuántos bytes ocupa `texto` codificado en UTF-8."""
    return len(texto.encode("utf-8"))


def razon_bytes_por_caracter(texto: str) -> float:
    """Devuelve bytes / caracteres. Lanza `ValueError` si `texto` está vacío."""
    if len(texto) == 0:
        raise ValueError("El texto no puede estar vacío.")
    return contar_bytes_utf8(texto) / len(texto)


if __name__ == "__main__":
    for muestra in ("hola", "ñandú", "Introducción a la visión", "🤖"):
        print(f"{muestra!r}: {len(muestra)} caracteres, "
            f"{contar_bytes_utf8(muestra)} bytes, "
            f"razón {razon_bytes_por_caracter(muestra):.2f}")