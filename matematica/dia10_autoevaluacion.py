"""Autoevaluación del Día 10: logaritmos, exponentes y sumatorias."""
import math


def verificar_ecuaciones() -> None:
    """Comprueba numéricamente las ecuaciones de la autoevaluación."""
    # 1. Cambio de base: log_5(1/1000)
    val_log5 = math.log10(1 / 1000) / math.log10(5)
    assert round(val_log5, 3) == -4.292

    # 2. Ecuación exponencial: 2450 = 2000 * e^(0.1 * t)
    t = (10 * math.log10(49 / 40)) / math.log10(math.e)
    assert math.isclose(2000 * math.exp(0.1 * t), 2450.0)

    # 3. Ecuación base 7: 5 * 7^(2y) = 175
    y = math.log(35, 7) / 2
    assert math.isclose(5 * (7 ** (2 * y)), 175.0)

    # 4. Ecuación base 10: 10^(2z/3) = 15
    z = (3 * math.log10(15)) / 2
    assert round(z, 3) == 1.764
    assert math.isclose(10 ** (2 * z / 3), 15.0)


def verificar_log_probabilidades() -> None:
    """Comprueba suma en escala logarítmica frente a underflow."""
    exponentes = [-120, -150, -80]
    producto_directo = 1.0
    for exp in exponentes:
        producto_directo *= 10.0 ** exp
    assert producto_directo == 0.0

    log10_total = sum(exponentes)
    assert log10_total == -350


def verificar_sumatorias_y_bpe() -> None:
    """Comprueba la sumatoria de impares y el conteo de bigramas."""
    suma_impares = sum(2 * k - 1 for k in range(1, 101))
    assert suma_impares == 10000

    palabras = ["robot", "robot", "roba"]
    pares: dict[str, int] = {}
    for palabra in palabras:
        for i in range(len(palabra) - 1):
            par = palabra[i:i + 2]
            pares[par] = pares.get(par, 0) + 1

    assert pares == {"ro": 3, "ob": 3, "bo": 2, "ot": 2, "ba": 1}


if __name__ == "__main__":
    verificar_ecuaciones()
    verificar_log_probabilidades()
    verificar_sumatorias_y_bpe()
    print("OK: autoevaluación del Día 10 verificada correctamente")
