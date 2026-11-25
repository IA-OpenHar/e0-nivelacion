"""B4 · Fricción y planos inclinados (unidades SI)."""
import math

G = 9.81  # m/s², gravedad estándar en superficie


def _validar_angulo(angulo_grados: float) -> None:
    """Valida que el ángulo esté en el intervalo [0, 90)."""
    if not 0 <= angulo_grados < 90:
        raise ValueError("El ángulo debe estar en [0, 90) grados.")


def friccion_estatica_max(masa: float, mu_s: float, g: float = G) -> float:
    """Fricción estática máxima en piso horizontal: mu_s·m·g (N).

    ValueError (mensaje en español) si masa <= 0 o mu_s < 0.
    """
    if masa <= 0:
        raise ValueError("La masa debe ser mayor que cero.")
    if mu_s < 0:
        raise ValueError("El coeficiente de fricción estática no puede ser negativo.")
    return mu_s * masa * g


def friccion_cinetica(masa: float, mu_k: float, g: float = G) -> float:
    """Fricción cinética en piso horizontal: mu_k·m·g (N).

    Mismas validaciones que friccion_estatica_max.
    """
    if masa <= 0:
        raise ValueError("La masa debe ser mayor que cero.")
    if mu_k < 0:
        raise ValueError("El coeficiente de fricción cinética no puede ser negativo.")
    return mu_k * masa * g


def aceleracion_horizontal(
    fuerza: float, masa: float, mu_s: float, mu_k: float, g: float = G
) -> float:
    """Aceleración (m/s²) de una caja en reposo empujada horizontalmente.

    Si la fuerza no supera la fricción estática máxima, la caja no se mueve
    y la aceleración es 0.0. Si la supera: (F - mu_k·m·g) / m.
    """
    f_estatica_max = friccion_estatica_max(masa, mu_s, g)
    f_cinetica = friccion_cinetica(masa, mu_k, g)

    if fuerza <= f_estatica_max:
        return 0.0
    return (fuerza - f_cinetica) / masa


def se_desliza(angulo_grados: float, mu_s: float) -> bool:
    """True si un bloque en reposo empieza a deslizar: tan θ > mu_s.

    ValueError si el ángulo no está en [0, 90).
    """
    _validar_angulo(angulo_grados)
    if mu_s < 0:
        raise ValueError("El coeficiente de fricción no puede ser negativo.")
    return math.tan(math.radians(angulo_grados)) > mu_s


def aceleracion_plano(angulo_grados: float, mu_k: float, g: float = G) -> float:
    """Aceleración (m/s²) de un bloque que ya baja por el plano.

    a = g·(sen θ - mu_k·cos θ). Si el resultado es <= 0, el bloque frena
    hasta detenerse: devuelve 0.0. ValueError si el ángulo no está en [0, 90).
    """
    _validar_angulo(angulo_grados)
    if mu_k < 0:
        raise ValueError("El coeficiente de fricción no puede ser negativo.")
    rad = math.radians(angulo_grados)
    acel = g * (math.sin(rad) - mu_k * math.cos(rad))
    return max(0.0, acel)


def aceleracion_maxima_sin_deslizar(mu_s: float, g: float = G) -> float:
    """Aceleración horizontal máxima que el piso permite sin resbalar: mu_s·g."""
    if mu_s < 0:
        raise ValueError("El coeficiente de fricción no puede ser negativo.")
    return mu_s * g


def distancia_frenado(velocidad: float, mu: float, g: float = G) -> float:
    """Distancia (m) para frenar desde `velocidad` solo con fricción: v²/(2·mu·g).

    ValueError si mu <= 0 o velocidad < 0.
    """
    if mu <= 0:
        raise ValueError("El coeficiente de fricción debe ser mayor que cero.")
    if velocidad < 0:
        raise ValueError("La velocidad no puede ser negativa.")
    return (velocidad ** 2) / (2 * mu * g)


if __name__ == "__main__":
    print(f"Fuerza para arrancar 10 kg con μs = 0.5: "
          f"{friccion_estatica_max(10, 0.5):.2f} N")
    print(f"¿Desliza a 30° con μs = 0.6? {se_desliza(30, 0.6)}")
    print(f"Robot a 1.5 m/s en piso mojado (μ = 0.3) frena en "
          f"{distancia_frenado(1.5, 0.3):.3f} m")
    print(f"Ángulo límite con μs = 0.6: "
          f"{math.degrees(math.atan(0.6)):.2f}°")
