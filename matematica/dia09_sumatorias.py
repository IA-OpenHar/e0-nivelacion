"""Comprobación para sumatorias y productorias del Día 9."""

import math


def problema_1():
    """Calcula las sumatorias básicas del Problema 1."""
    suma_lineal = sum(range(1, 6))
    suma_cuadrados = sum(i**2 for i in range(1, 5))
    return suma_lineal, suma_cuadrados


def problema_2():
    """Calcula la suma de Gauss (1..100) y la serie (1..550)."""
    gauss_100 = sum(range(1, 101))
    serie_550 = sum(2 * k + 50 for k in range(1, 551))
    return gauss_100, serie_550


def problema_3():
    """Calcula productoria 1..5 y verifica ln(Pi) = sum(ln(pi))."""
    prod_5 = math.prod(range(1, 6))
    probs = [0.5, 0.25, 0.8]
    prod_prob = math.prod(probs)
    ln_prod = math.log(prod_prob)
    suma_ln = sum(math.log(p) for p in probs)
    return prod_5, prod_prob, ln_prod, suma_ln


def problema_4():
    """Calcula la media de x y el Error Cuadrático Medio (MSE)."""
    x = [2, 4, 9]
    media_x = sum(x) / len(x)

    y = [3, 5]
    y_pred = [2.5, 5.5]
    mse = sum((r - p) ** 2 for r, p in zip(y, y_pred)) / len(y)
    return media_x, mse


def problema_5():
    """Calcula multiplicaciones para matrices 1000x1000."""
    n = 1000
    return n**3


def problema_6():
    """Comprueba los problemas 2 y 3 usando sum y math.prod."""
    comp_gauss = sum(range(1, 101))
    comp_serie = sum(2 * k + 50 for k in range(1, 551))
    comp_prod = math.prod(range(1, 6))
    return comp_gauss, comp_serie, comp_prod


def main():
    """Ejecuta y muestra los resultados de todos los problemas."""
    p1_lin, p1_cuad = problema_1()
    print(f"P1 -> Suma 1..5: {p1_lin} | Cuadrados 1..4: {p1_cuad}")

    p2_gauss, p2_serie = problema_2()
    print(f"P2 -> Gauss 1..100: {p2_gauss} | Serie 1..550: {p2_serie}")

    p3_prod, p3_prob, p3_ln1, p3_ln2 = problema_3()
    print(
        f"P3 -> Prod 1..5: {p3_prod} | Prob: {p3_prob:.4f} | "
        f"ln(Pi): {p3_ln1:.4f} | Sum ln: {p3_ln2:.4f}"
    )

    p4_media, p4_mse = problema_4()
    print(f"P4 -> Media: {p4_media} | MSE: {p4_mse}")

    p5_mult = problema_5()
    print(f"P5 -> Multiplicaciones (1000x1000): {p5_mult:,}")

    p6_gauss, p6_serie, p6_prod = problema_6()
    print(
        f"P6 -> sum(1..100): {p6_gauss} | "
        f"serie: {p6_serie} | prod(1..5): {p6_prod}"
    )


if __name__ == "__main__":
    main()
