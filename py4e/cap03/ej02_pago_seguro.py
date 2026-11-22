import sys

try:
    horas = float(input('Introduce las horas: '))
    tarifa = float(input('Introduce la tarifa por hora: '))
except ValueError:
    print('Error, introduce un valor numerico')
    sys.exit(1)
    
if horas <= 40: 
    pago = horas * tarifa
else:
    horas_extras = horas - 40
    pago = (40 * tarifa) + (horas_extras * tarifa * 1.5)
    
print(f'Pago: {pago:.2f}')