import sys

try:
    horas = float(input('Introduce las horas: '))
    tarifa = float(input('Introduce la tarifa por hora: '))
except ValueError:
    print('Error: Por favor, introduce valores numéricos válidos.')
    sys.exit(1)

if horas < 0 or tarifa < 0:
    print('Error, las horas y la tarifa deben ser valores negativos')
    sys.exit(1)
    
pago = horas * tarifa
print(f'Pago: {pago:.2f}')