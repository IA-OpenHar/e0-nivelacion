"""Módulo de comprobación para los problemas de sumatorias y productorias del Día 9."""

import math


def problema_1():
    """Calcula las sumatorias básicas del Problema 1."""
    suma_lineal = sum(range(1, 6))
    suma_cuadrados = sum(i**2 for i in range(1, 5))
    return suma_lineal, suma_cuadrados


def problema_2():
    """Calcula la suma de Gauss (1 a 100) y la serie aritmética (1 a 550)."""
    gauss_100 = sum(range(1, 101))
    serie_550 = sum(2 * k + 50 for k in range(1, 551))
    return gauss_100, serie_550


def problema_3():
    """Calcula la productoria 1 a 5 y verifica la propiedad ln(Pi) = sum(ln(pi))."""
    prod_5 = math.prod(range(1, 6))
    probabilidades = [0.5, 0.25, 0.8]
    prod_prob = math.prod(probabilidades)
    ln_prod = math.log(prod_prob)
    suma_ln = sum(math.log(p) for p in probabilidades)
    return prod_5, prod_prob, ln_prod, suma_ln


def problema_4():
    """Calcula la media de x y el Error Cuadrático Medio (MSE)."""
    x = [2, 4, 9]
    media_x = sum(x) / len(x)

    y = [3, 5]
    y_pred = [2.5, 5.5]
    mse = sum((real - pred) ** 2 for real, pred in zip(y, y_pred)) / len(y)
    return media_x, mse


def problema_5():
    """Calcula el total de multiplicaciones directas para matrices 1000x1000."""
    n = 1000
    return n**3


def problema_6():
    """Comprueba los problemas 2 y 3 usando sum y math.prod como pide la guía."""
    comp_gauss = sum(range(1, 101))
    comp_serie = sum(2 * k + 50 for k in range(1, 551))
    comp_prod = math.prod(range(1, 6))
    return comp_gauss, comp_serie, comp_prod


def main():
    """Ejecuta y muestra los resultados de todos los problemas."""
    p1_lin, p1_cuad = problema_1()
    print(f"Problema 1 -> Suma 1..5: {p1_lin} | Suma cuadrados 1..4: {p1_cuad}")

    p2_gauss, p2_serie = problema_2()
    print(f"Problema 2 -> Gauss 1..100: {p2_gauss} | Serie 1..550: {p2_serie}")

    p3_prod, p3_prob, p3_ln1, p3_ln2 = problema_3()
    print(
        f"Problema 3 -> Prod 1..5: {p3_prod} | Prod prob: {p3_prob:.4f} | "
        f"ln(Pi): {p3_ln1:.4f} | Sum ln(p): {p3_ln2:.4f}"
    )

    p4_media, p4_mse = problema_4()
    print(f"Problema 4 -> Media: {p4_media} | MSE: {p4_mse}")

    p5_mult = problema_5()
    print(f"Problema 5 -> Multiplicaciones (1000x1000): {p5_mult:,}")

    p6_gauss, p6_serie, p6_prod = problema_6()
    print(
        f"Problema 6 (Comprobación) -> sum(1..100): {p6_gauss} | "
        f"sum(serie): {p6_serie} | math.prod(1..5): {p6_prod}"
    )


if __name__ == "__main__":
    main()
