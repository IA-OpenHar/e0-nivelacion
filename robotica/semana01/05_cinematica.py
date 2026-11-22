"""Funciones de cinemática 1D para problemas de robótica."""
import math


def distancia_frenado(v0: float, a: float) -> float:
    """Devuelve v0^2 / (2 * |a|); a entra negativo."""
    return (v0 ** 2) / (2 * abs(a))


def tiempo_impacto(h0: float, v0: float, g: float = 9.81) -> float:
    """Raíz positiva de h0 + v0*t - 0.5*g*t^2 = 0 con la fórmula cuadrática."""
    discriminante = (v0 ** 2) + 2 * g * h0
    return (v0 + math.sqrt(discriminante)) / g


def tiempo_trapezoidal(d: float, v_max: float, a: float) -> float:
    """Duración total del perfil trapezoidal (o triangular si d < v_max^2 / a)."""
    d_acel_freno = (v_max ** 2) / a
    # Caso borde: el tramo es tan corto que no alcanza v_max (perfil triangular)
    if d < d_acel_freno:
        return 2 * math.sqrt(d / a)

    # Caso normal: perfil trapezoidal (acelera + velocidad crucero + frena)
    t_acel = v_max / a
    d_crucero = d - d_acel_freno
    t_crucero = d_crucero / v_max
    return 2 * t_acel + t_crucero


if __name__ == '__main__':
    # 1. Pruebas de la tabla de la guía
    assert math.isclose(distancia_frenado(1.2, -0.4), 1.8)
    assert math.isclose(tiempo_impacto(10, 3), 1.766, rel_tol=1e-3)
    assert math.isclose(tiempo_impacto(20, 0), 2.019275109384609)
    assert math.isclose(tiempo_trapezoidal(0.30, 0.4, 2), 0.95)
    # Caso borde triangular
    assert math.isclose(tiempo_trapezoidal(0.05, 0.4, 2), 0.31622776601683794)

    print("Todas las pruebas de cinematica.py pasan.")
