"""Ejercicio 3: Busqueda binaria con presupuesto de intentos."""

def comparar(intento: int, secreto: int) -> int:
    """Herramienta: -1 si el intento es bajo, 1 si es alto, o si acierta."""
    if intento == secreto:
        return 0
    return -1 if intento < secreto else 1

def buscar_con_presupuesto(secreto: int, minimo: int, maximo: int,
                           max_pasos: int) -> int:
    """Llama a comprar() con el punto medio del rango hasta acertar.
    
    Devuelve los pasos usados, o -1 se se agota max_pasos o el rango queda vacio.
    """
    pasos = 0
    while pasos < max_pasos and minimo <= maximo:
        pasos += 1
        medio = (minimo + maximo) // 2
        resultado = comparar(medio, secreto)
        
        if resultado == 0:
            return pasos
        if resultado == -1:
            minimo = medio +1
        else:
            maximo = medio -1
            
    return -1

if __name__ == '__main__':
    assert buscar_con_presupuesto(37, 1, 100, 10) == 3
    assert buscar_con_presupuesto(1, 1, 100, 10) == 6
    assert buscar_con_presupuesto(100, 1, 100, 10) == 7
    assert buscar_con_presupuesto(37, 1, 100, 2) == -1
    assert buscar_con_presupuesto(150, 1, 100, 10) == -1
    print('Todas las prueban pasan')
    
    peor_caso = 0
    for s in range(1, 101):
        intentos = buscar_con_presupuesto(s, 1, 100, 10)
        if intentos > peor_caso:
            peor_caso = intentos
    print('Peor caso de 1 a 100:', peor_caso)
    