"""Ejercicio 5: Verificar si un número entero es primo."""
def es_primo(n: int) -> bool:
    """Devuelve True si n es primo, False en caso contrario."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    assert es_primo(2) is True
    assert es_primo(9) is False
    assert es_primo(1) is False
    assert es_primo(97) is True
    print('Todas las pruebas pasan')
