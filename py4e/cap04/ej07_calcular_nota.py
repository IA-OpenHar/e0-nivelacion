"""Convierte un puntaje numerico (0.0 a 1.0) a una calificacion en letra."""

def calcular_nota(puntaje):
    """Dvuelve la letra de calificacion (A-F) o Bad score si esta fuera de rango."""
    if puntaje < 0.0 or puntaje > 1.0:
        return 'Bad score'
    if puntaje >= 0.9:
        return 'A'
    if puntaje >= 0.8:
        return 'B'
    if puntaje >= 0.7:
        return 'C'
    if puntaje >= 0.6:
        return 'D'
    return 'F'


if __name__ == "__main__":
    try:
        entrada = float(input('Puntaje (0.0 a 1.0): '))
        print(calcular_nota(entrada))
    except ValueError:
        print('Bad score')
