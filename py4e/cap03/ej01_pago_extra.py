horas = float(input('Introduce las horas: '))
tarifa = float(input('Introduce la tarifa por hora: '))

if horas <=40:
    pago = horas * tarifa
else: 
    horas_extra = horas - 40
    pago = (40 * tarifa) + (horas_extra * tarifa * 1.5)
    
print(f'Pago: {pago:.2f}')