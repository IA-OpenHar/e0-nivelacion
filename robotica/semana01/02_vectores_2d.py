"""Cálculo de vectores en 2D y movimiento básico de un robot móvil."""
import math


def magnitud(vx: float, vy: float) -> float:
    """Devuelve la magnitud sqrt(vx^2 + vy^2) del vector."""
    return math.hypot(vx, vy)  # Equivale a math.sqrt(vx**2 + vy**2)


def direccion_grados(vx: float, vy: float) -> float:
    """Devuelve el ángulo del vector en grados usando math.atan2."""
    radianes = math.atan2(vy, vx)
    return math.degrees(radianes)


def componentes(v: float, angulo_grados: float) -> tuple[float, float]:
    """Convierte magnitud v y ángulo en grados a componentes (vx, vy)."""
    radianes = math.radians(angulo_grados)
    vx = v * math.cos(radianes)
    vy = v * math.sin(radianes)
    return (vx, vy)


def mover(x: float, y: float, v: float, angulo_grados: float, t: float) -> tuple[float, float]:
    """Devuelve la nueva posición (x, y) tras moverse a velocidad v y rumbo dado durante t segundos."""
    vx, vy = componentes(v, angulo_grados)
    nuevo_x = x + vx * t
    nuevo_y = y + vy * t
    return (nuevo_x, nuevo_y)


if __name__ == '__main__':
    # 1. Pruebas de la tabla de la guía
    assert math.isclose(magnitud(3, 4), 5.0, abs_tol=1e-9)
    assert math.isclose(direccion_grados(1, 1), 45.0, abs_tol=1e-9)
    assert math.isclose(direccion_grados(-1, 0), 180.0, abs_tol=1e-9)

    cx, cy = componentes(2, 90)
    assert math.isclose(cx, 0.0, abs_tol=1e-9)
    assert math.isclose(cy, 2.0, abs_tol=1e-9)

    px1, py1 = mover(0, 0, 0.5, 0, 4)
    assert math.isclose(px1, 2.0, abs_tol=1e-9)
    assert math.isclose(py1, 0.0, abs_tol=1e-9)

    px2, py2 = mover(0, 0, 1, 90, 2)
    assert math.isclose(px2, 0.0, abs_tol=1e-9)
    assert math.isclose(py2, 2.0, abs_tol=1e-9)

    print("Todas las pruebas de vectores_2d pasan.")

    # 2. Reto de la guía: parte de (1, 1), avanza a 2 m/s con rumbo 45° durante 3 s
    x_final, y_final = mover(1, 1, 2, 45, 3)
    print(f"Posición final del reto: ({x_final:.2f}, {y_final:.2f})")
