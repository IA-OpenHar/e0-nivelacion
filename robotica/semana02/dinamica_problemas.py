"""B4 · Problemas de dinámica: poleas, mesa con polea y plano con fricción."""
import math

G = 9.81  # m/s², gravedad estándar en superficie


def _validar_masas(*masas: float) -> None:
    """Valida que todas las masas sean estrictamente positivas."""
    for m in masas:
        if m <= 0:
            raise ValueError("La masa debe ser mayor que cero")


def _validar_mu_k(mu_k: float) -> None:
    """Valida que el coeficiente de fricción cinética no sea negativo."""
    if mu_k < 0:
        raise ValueError(
            "El coeficiente de fricción mu_k no puede ser negativo"
        )


def aceleracion_atwood(m1: float, m2: float, g: float = G) -> float:
    """Aceleración (m/s²) de una máquina de Atwood ideal.

    Dos masas cuelgan de una polea sin fricción ni masa. Positiva si
    m1 baja: a = (m1 - m2)·g / (m1 + m2).
    ValueError (mensaje en español) si alguna masa <= 0.
    """
    _validar_masas(m1, m2)
    return (m1 - m2) * g / (m1 + m2)


def tension_atwood(m1: float, m2: float, g: float = G) -> float:
    """Tensión (N) de la cuerda en la máquina de Atwood.

    T = 2·m1·m2·g / (m1 + m2). ValueError si alguna masa <= 0.
    """
    _validar_masas(m1, m2)
    return 2 * m1 * m2 * g / (m1 + m2)


def aceleracion_mesa_polea(
    m_mesa: float, m_colgante: float, mu_k: float, g: float = G
) -> float:
    """Aceleración (m/s²) de un bloque en una mesa jalado por otro colgante.

    La cuerda pasa por una polea ideal en el borde de la mesa. Fuerza
    neta = m_colgante·g - mu_k·m_mesa·g. Si no es positiva, el sistema
    no arranca: devuelve 0.0. Si lo es, a = neta / (m_mesa + m_colgante).
    ValueError si alguna masa <= 0 o mu_k < 0.
    """
    _validar_masas(m_mesa, m_colgante)
    _validar_mu_k(mu_k)
    neta = m_colgante * g - mu_k * m_mesa * g
    if neta <= 0:
        return 0.0
    return neta / (m_mesa + m_colgante)


def tension_mesa_polea(
    m_mesa: float, m_colgante: float, mu_k: float, g: float = G
) -> float:
    """Tensión (N) de la cuerda en el sistema mesa-polea.

    Del bloque colgante: T = m_colgante·(g - a), con la a de
    aceleracion_mesa_polea. Mismas validaciones.
    """
    a = aceleracion_mesa_polea(m_mesa, m_colgante, mu_k, g)
    return m_colgante * (g - a)


def rapidez_final_plano(
    altura: float, angulo_grados: float, mu_k: float, g: float = G
) -> float:
    """Rapidez (m/s) al pie de un plano, partiendo del reposo.

    Por energía con fricción: v² = 2·g·h·(1 - mu_k / tan θ).
    Si v² <= 0, el bloque no llega a moverse: devuelve 0.0.
    ValueError si altura < 0, mu_k < 0 o el ángulo no está en (0, 90).
    """
    if altura < 0:
        raise ValueError("La altura no puede ser negativa")
    _validar_mu_k(mu_k)
    if angulo_grados <= 0 or angulo_grados >= 90:
        raise ValueError("El ángulo debe estar entre 0 y 90 grados")
    tan_theta = math.tan(math.radians(angulo_grados))
    v_cuadrado = 2 * g * altura * (1 - mu_k / tan_theta)
    if v_cuadrado <= 0:
        return 0.0
    return math.sqrt(v_cuadrado)


def potencia_subida(
    masa: float, altura: float, tiempo: float, g: float = G
) -> float:
    """Potencia media (W) para subir `masa` una `altura` en `tiempo`.

    Solo cuenta el trabajo contra la gravedad: m·g·h / t.
    ValueError si masa <= 0 o tiempo <= 0.
    """
    _validar_masas(masa)
    if tiempo <= 0:
        raise ValueError("El tiempo debe ser mayor que cero")
    return masa * g * altura / tiempo


if __name__ == "__main__":
    print(
        f"Atwood 5 y 3 kg: a = {aceleracion_atwood(5, 3):.4f} m/s², "
        f"T = {tension_atwood(5, 3):.4f} N"
    )
    print(
        f"Mesa 4 kg, colgante 2 kg, mu 0.2: "
        f"a = {aceleracion_mesa_polea(4, 2, 0.2):.3f} m/s²"
    )
    print(
        f"Plano 2 m a 30°, mu 0.2: "
        f"v = {rapidez_final_plano(2, 30, 0.2):.3f} m/s"
    )
    print(f"Subir 60 kg 3 m en 6 s: {potencia_subida(60, 3, 6):.1f} W")
