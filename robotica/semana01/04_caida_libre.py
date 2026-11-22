"""Bloque B4: Caída libre analítica y simulación por integración de Euler."""

import math

G = 9.81

def altura(h0: float, t: float) -> float:
    """Devuelve la altura y(t) en metros tras t segundos."""
    return h0 - 0.5 * G * (t ** 2)

def tiempo_caida(h0: float) -> float:
    """Devuelve el tiempo exacto en segundos hasta tocar el suelo (y = 0)."""
    return math.sqrt(2 * h0 / G)


def rapidez_impacto(h0: float) -> float:
    """Devuelve la rapidez (magnitud de velocidad) al llegar al suelo en m/s."""
    return math.sqrt(2 * G * h0)

def simular_caida(h0: float, dt: float) -> float:
    """Simula la caída paso a paso con Euler semi-implícito y devuelve el tiempo."""
    y = h0
    v = 0.0
    t = 0.0

    while y > 0:
        v = v - G * dt
        y = y + v * dt
        t = t + dt

    return t

if __name__ == '__main__':
    # 1. Pruebas de las fórmulas exactas (tabla de la guía)
    assert round(altura(20, 1), 3) == 15.095
    assert round(tiempo_caida(20), 3) == 2.019
    assert round(rapidez_impacto(20), 3) == 19.809
    print('Pruebas analíticas correctas.\n')

    # 2. Comparación simulación vs. valor exacto para h0 = 20 m
    t_exacto = tiempo_caida(20)
    print(f"Tiempo exacto: {t_exacto:.4f} s\n")
    print(f"{'Paso dt (s)':<14} {'Tiempo simulado (s)':<22} {'Error absoluto (s)'}")
    print("-" * 58)

    for paso in [0.1, 0.01, 0.001]:
        t_sim = simular_caida(20, paso)
        error = abs(t_sim - t_exacto)
        print(f"{paso:<14} {t_sim:<22.3f} {error:.4f}")
