"""B4 · Leyes de Newton: fuerza, masa, aceleración y peso (unidades SI)."""

G = 9.81  # m/s², gravedad estándar en superficie
KG_POR_LIBRA = 0.45359237  # definición exacta de la libra avoirdupois


def _validar_masa(masa: float) -> None:
    if masa <= 0:
        raise ValueError("La masa debe ser mayor que 0.")


def aceleracion(fuerza_neta: float, masa: float) -> float:
    """a = F/m en m/s². ValueError si masa <= 0."""
    _validar_masa(masa)
    return fuerza_neta / masa


def fuerza_neta(masa: float, aceleracion_ms2: float) -> float:
    """F = m·a en N. ValueError si masa <= 0."""
    _validar_masa(masa)
    return masa * aceleracion_ms2


def peso(masa: float, g: float = G) -> float:
    """W = m·g en N. ValueError si masa <= 0."""
    _validar_masa(masa)
    return masa * g


def normal_ascensor(masa: float, aceleracion_ms2: float, g: float = G) -> float:
    """Fuerza normal (N) del piso de un ascensor sobre una persona.

    aceleracion_ms2 > 0 significa acelerando hacia arriba. N = m·(g + a).
    ValueError si masa <= 0 o si N resulta negativa (la persona se despega).
    """
    _validar_masa(masa)
    normal = masa * (g + aceleracion_ms2)
    if normal < -1e-9:
        raise ValueError("La fuerza normal no puede ser negativa (la persona se despega).")
    return max(0.0, normal)


def suma_fuerzas(fuerzas: list[tuple[float, float]]) -> tuple[float, float]:
    """Suma vectorial de fuerzas (Fx, Fy) en N. Lista vacía -> (0.0, 0.0)."""
    fx_total = 0.0
    fy_total = 0.0
    for fx, fy in fuerzas:
        fx_total += fx
        fy_total += fy
    return (fx_total, fy_total)


def libras_a_kg(libras: float) -> float:
    """Convierte libras a kilogramos."""
    return libras * KG_POR_LIBRA

if __name__ == "__main__":
    caja = libras_a_kg(154)
    print(f"Caja de 154 lb = {caja:.2f} kg; fuerza para sostenerla: {peso(caja):.1f} N")
    print(f"Persona de 70 kg, ascensor subiendo a 1.5 m/s²: N = {normal_ascensor(70, 1.5):.1f} N")
