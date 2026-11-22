"""Calculadora de línea de comandos: modo argumentos y modo interactivo."""
import math
import sys

# Tupla y no lista: los operadores no deben cambiar mientras corre el programa
OPERADORES = ('+', '-', '*', '/', '**')


def calcular(a: float, op: str, b: float) -> float:
    """Devuelve a op b.

    Lanza ValueError si op no es válido o si el resultado es complejo.
    """
    if op not in OPERADORES:
        raise ValueError(f"operador no válido '{op}'. Usa: + - * / **")

    if op == '+':
        resultado = a + b
    elif op == '-':
        resultado = a - b
    elif op == '*':
        resultado = a * b
    elif op == '/':
        resultado = a / b
    else:
        resultado = a ** b

    if isinstance(resultado, complex):
        raise ValueError("el resultado no es un número real")

    return resultado

def interpretar(linea: str) -> tuple[float, str, float]:
    """Convierte '3 + 4' o '3+4' en (3.0, '+', 4.0)."""
    texto = linea.strip()
    partes = texto.split()

    if len(partes) == 3:
        str_a, op, str_b = partes
    else:
        str_a, op, str_b = '', '', ''
        i = 1  # Empezamos en 1 para permitir signo negativo/positivo en el primer número
        while i < len(texto):
            if texto[i:i + 2] == '**':
                str_a, op, str_b = texto[:i], '**', texto[i + 2:]
                break
            if texto[i] in ('+', '-', '*', '/'):
                str_a, op, str_b = texto[:i], texto[i], texto[i + 1:]
                break
            i += 1

    if not str_a.strip() or not op or not str_b.strip():
        raise ValueError("escribe <a> <op> <b>")

    a = float(str_a)
    b = float(str_b)

    if not (math.isfinite(a) and math.isfinite(b)):
        raise ValueError("no se permiten valores 'nan' ni 'inf'")

    return (a, op, b)


def formatear(x: float) -> str:
    """Muestra 7.0 como '7' y 3.5 como '3.5'. Pista: x.is_integer()."""
    if x.is_integer():
        return str(int(x))
    return str(x)


def main() -> int:
    """Con 3 argumentos calcula una vez; sin ellos, modo interactivo."""
    # 1. Modo argumentos: python3 calculadora.py 3 + 4
    if len(sys.argv) == 4:
        try:
            linea = ' '.join(sys.argv[1:])
            a, op, b = interpretar(linea)
            resultado = calcular(a, op, b)
            print(formatear(resultado))
            return 0
        except ZeroDivisionError:
            print("Error: división entre cero", file=sys.stderr)
            return 1
        except OverflowError:
            print("Error: resultado fuera de rango", file=sys.stderr)
            return 1
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1

    # 2. Modo interactivo: python3 calculadora.py
    if len(sys.argv) == 1:
        ans = 0.0
        try:
            while True:
                linea = input('calc> ')
                if linea.strip() == 'salir':
                    return 0
                if not linea.strip():
                    continue
                try:
                    linea_con_ans = linea.replace('ans', str(ans))
                    a, op, b = interpretar(linea_con_ans)
                    resultado = calcular(a, op, b)
                    ans = resultado
                    print(formatear(resultado))
                except ZeroDivisionError:
                    print("Error: división entre cero")
                except OverflowError:
                    print("Error: resultado fuera de rango")
                except ValueError as e:
                    print(f"Error: {e}")
        except (EOFError, KeyboardInterrupt):
            print()
            return 0

    # 3. Cualquier otro número de argumentos
    print("Uso: python3 calculadora.py <a> <op> <b>", file=sys.stderr)
    return 2

if __name__ == '__main__':
    sys.exit(main())
# prueba git