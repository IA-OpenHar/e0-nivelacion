"""Ejercicio 8: Imprimir la tabla de multiplicar de n del 1 al 10."""
def tabla(n: int) -> None:
    """Imprime la tabla de multiplicar de n, del 1 al 10."""
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

if __name__ == '__main__':
    tabla(7)
