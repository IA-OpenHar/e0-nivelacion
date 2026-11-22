"""Calcula el pago semanal aplicando recargo de 1.5x a las horas extras."""

def calcular_pago(horas, tarifa):
    """Devuelve el pago total; las horas sobre 40 se pagan a 1.5 veces la tarifa."""
    if horas > 40:
        horas_extras = horas - 40
        return (40 * tarifa) + (horas_extras * tarifa * 1.5)
    return horas * tarifa


if __name__ == "__main__":
    horas_trabajadas = float(input('Horas: '))
    tarifa_hora = float(input('tarifa:'))
    print(f'Pago: {calcular_pago(horas_trabajadas, tarifa_hora):.2f}')
    