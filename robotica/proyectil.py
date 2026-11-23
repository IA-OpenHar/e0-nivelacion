"""B4 · Cinemática 2D: tiro parabólico sin rozamiento del aire."""
import math

G = 9.81  # m/s², valor estándar en superficie; cámbialo solo si el problema lo pide


def _validar_entradas(v0: float, angulo_grados: float, h0: float = 0.0, g: float = G) -> None:
    """Valida que los parámetros físicos estén dentro de rangos válidos."""
    if v0 < 0 or not (0.0 <= angulo_grados <= 90.0) or h0 < 0 or g <= 0:
        raise ValueError("Parámetros inválidos: v0 >= 0, 0 <= ángulo <= 90, h0 >= 0, g > 0.")


def componentes(v0: float, angulo_grados: float) -> tuple[float, float]:
    """Devuelve (vx, vy) en m/s de una velocidad v0 con ángulo sobre la horizontal."""
    _validar_entradas(v0, angulo_grados)
    rad = math.radians(angulo_grados)
    return v0 * math.cos(rad), v0 * math.sin(rad)


def tiempo_vuelo(v0: float, angulo_grados: float, h0: float = 0.0, g: float = G) -> float:
    """Tiempo (s) hasta tocar el suelo (y = 0) desde la altura h0."""
    _validar_entradas(v0, angulo_grados, h0, g)
    _, vy0 = componentes(v0, angulo_grados)
    return (vy0 + math.sqrt(vy0 ** 2 + 2 * g * h0)) / g


def alcance(v0: float, angulo_grados: float, h0: float = 0.0, g: float = G) -> float:
    """Distancia horizontal (m) recorrida hasta tocar el suelo."""
    _validar_entradas(v0, angulo_grados, h0, g)
    vx, _ = componentes(v0, angulo_grados)
    t = tiempo_vuelo(v0, angulo_grados, h0, g)
    return vx * t


def altura_maxima(v0: float, angulo_grados: float, h0: float = 0.0, g: float = G) -> float:
    """Altura máxima (m) medida desde el suelo: h0 + vy²/(2g)."""
    _validar_entradas(v0, angulo_grados, h0, g)
    _, vy0 = componentes(v0, angulo_grados)
    return h0 + (vy0 ** 2) / (2 * g)


def alcance_euler(v0: float, angulo_grados: float, h0: float = 0.0,
                dt: float = 0.001, g: float = G) -> float:
    """Alcance (m) por integración numérica con Euler semi-implícito (Día 4)."""
    _validar_entradas(v0, angulo_grados, h0, g)
    if dt <= 0:
        raise ValueError("dt debe ser positivo.")

    vx, vy = componentes(v0, angulo_grados)
    x = 0.0
    y = h0

    while y >= 0.0:
        vy -= g * dt
        x += vx * dt
        y += vy * dt

    return x


if __name__ == "__main__":
    for ang in (30.0, 45.0, 60.0):
        print(f"{ang:>4.0f}°  t = {tiempo_vuelo(20.0, ang):.3f} s  "
            f"R = {alcance(20.0, ang):.3f} m  H = {altura_maxima(20.0, ang):.3f} m")
    print(f"Euler (dt = 1 ms) a 45°: R = {alcance_euler(20.0, 45.0):.3f} m")