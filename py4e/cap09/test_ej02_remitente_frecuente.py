"""Pruebas de ej02_remitente_frecuente.

Ejecutar: python test_ej02_remitente_frecuente.py
"""

from ej02_remitente_frecuente import dominios, remitente_frecuente, remitentes

LINEAS = [
    "From ana@robot.pe Sat Jan  5 09:14:16 2008\n",
    "From: ana@robot.pe\n",
    "Subject: prueba\n",
    "From luis@lab.edu Fri Jan  4 18:10:48 2008\n",
    "From ana@robot.pe Fri Jan  4 16:10:39 2008\n",
    "From eva@lab.edu Fri Jan  4 15:46:24 2008\n",
    "Fromage no es un remitente\n",
]


def test_remitentes() -> None:
    conteo = remitentes(LINEAS)
    # "From:" y "Fromage" no cuentan: solo "From " con espacio.
    assert conteo == {"ana@robot.pe": 2, "luis@lab.edu": 1, "eva@lab.edu": 1}
    assert remitentes([]) == {}


def test_remitente_frecuente() -> None:
    assert remitente_frecuente(remitentes(LINEAS)) == ("ana@robot.pe", 2)
    # Empate: gana el primero que aparece.
    assert remitente_frecuente({"x@a.pe": 1, "y@b.pe": 1}) == ("x@a.pe", 1)
    try:
        remitente_frecuente({})
    except ValueError:
        pass
    else:
        raise AssertionError("Debió lanzar ValueError")


def test_dominios() -> None:
    assert dominios(remitentes(LINEAS)) == {"robot.pe": 2, "lab.edu": 2}
    assert dominios({}) == {}


if __name__ == "__main__":
    test_remitentes()
    test_remitente_frecuente()
    test_dominios()
    print("OK: 3 pruebas de ej02_remitente_frecuente")
