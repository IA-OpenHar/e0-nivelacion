# Frecuencia de palabras

## Qué hace
Lee un archivo de texto en UTF-8, normaliza las palabras eliminando signos de puntuación y muestra las N palabras más frecuentes con su cantidad y porcentaje.

## Cómo usarlo
```bash
python frecuencia.py datos/ejemplo.txt 5
```

## Ejemplo de salida
```text
 1. el                 9   7.9 %
 2. un                 6   5.3 %
 3. no                 5   4.4 %
 4. robot              5   4.4 %
 5. y                  5   4.4 %
Total: 114 palabras, 67 distintas
```

## Cómo correr las pruebas
```bash
python test_frecuencia.py
```

## Qué aprendí
Aprendí a combinar diccionarios, ordenamiento con tuplas negativas y `lambda`, formateo de columnas con f-strings y manejo de códigos de salida y errores por `sys.stderr`.
