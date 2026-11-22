import sys
try:
    celsius = float(input('IIntroduce la temperatura en Celsius: '))
except ValueError:
    print('Error: Por favor, introduce un valor numérico válido.')
    sys.exit(1)
    
if celsius < -273.15:
    print('Error, la temperatura no puede estar por debajo de -273.15 °C')
    sys.exit(1)
    
fahrenheit = celsius * 9 / 5 + 32
print(f'Temperatura en Fahrenheit: {fahrenheit:.1f}')