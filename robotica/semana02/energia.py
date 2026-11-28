"""B4 · Trabajo, energía y potencia (unidades SI)."""

import math

G = 9.81  # m/s², gravedad estándar en superficie


def _validar_positivo(valor: float, nombre: str) -> None:
    """Lanza ValueError si el valor es menor o igual a cero."""
    if valor <= 0:
        raise ValueError(f"{nombre} debe ser mayor que cero.")


def trabajo(fuerza: float, distancia: float, angulo_grados: float = 0.0) -> float:
    """Trabajo (J) de una fuerza constante: F · d · cos θ.

    θ es el ángulo entre la fuerza y el desplazamiento.
    ValueError (mensaje en español) si distancia < 0.
    """
    if distancia < 0:
        raise ValueError("La distancia no puede ser negativa.")
    return fuerza * distancia * math.cos(math.radians(angulo_grados))


def energia_cinetica(masa: float, velocidad: float) -> float:
    """Energía cinética (J): ½ · m · v².

    ValueError si masa <= 0.
    """
    _validar_positivo(masa, "La masa")
    return 0.5 * masa * (velocidad**2)


def energia_potencial(masa: float, altura: float, g: float = G) -> float:
    """Energía potencial gravitacional (J): m · g · h.

    ValueError si masa <= 0.
    """
    _validar_positivo(masa, "La masa")
    return masa * g * altura


def velocidad_tras_caida(altura: float, g: float = G) -> float:
    """Rapidez (m/s) al caer desde altura sin fricción: √(2 g h).

    Sale de igualar m g h = ½ m v² (la masa se cancela).
    ValueError si altura < 0.
    """
    if altura < 0:
        raise ValueError("La altura no puede ser negativa.")
    return math.sqrt(2 * g * altura)


def potencia(trabajo_j: float, tiempo_s: float) -> float:
    """Potencia media (W): trabajo / tiempo. ValueError si tiempo <= 0."""
    _validar_positivo(tiempo_s, "El tiempo")
    return trabajo_j / tiempo_s


def autonomia_horas(energia_kwh: float, potencia_w: float) -> float:
    """Horas que dura una batería de energia_kwh a potencia_w vatios.

    1 kWh = 1000 W durante 1 hora. ValueError si potencia_w <= 0.
    """
    _validar_positivo(potencia_w, "La potencia")
    energia_wh = energia_kwh * 1000.0
    return energia_wh / potencia_w


if __name__ == "__main__":
    print(f"Trabajo 50 N, 4 m: {trabajo(50, 4):.1f} J")
    print(f"Ec de 2 kg a 3 m/s: {energia_cinetica(2, 3):.1f} J")
    print(f"Rapidez tras caer 5 m: {velocidad_tras_caida(5):.3f} m/s")
    print(f"Batería de 2.3 kWh a 460 W: {autonomia_horas(2.3, 460):.1f} h")
