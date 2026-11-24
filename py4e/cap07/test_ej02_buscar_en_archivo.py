"""Pruebas de ej02_buscar_en_archivo. Ejecutar: python test_ej02_buscar_en_archivo.py"""
import math
import os
import tempfile

from ej02_buscar_en_archivo import lineas_que_empiezan, promedio_confianza

MUESTRA = (
    "From ana@uni.edu Sat Jan  5 09:14:16 2008\n"
    "Subject: prueba\n"
    "X-DSPAM-Confidence: 0.8475\n"
    "From: ana@uni.edu\n"
    "From luis@uni.edu Fri Jan  4 18:10:48 2008\n"
    "X-DSPAM-Confidence: 0.6178\n"
)
def _crear(carpeta: str, texto: str) -> str:
    ruta = os.path.join(carpeta, "mini_mbox.txt")
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write(texto)
    return ruta
def test_filtrar() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        ruta = _crear(tmp, MUESTRA)
        # 'From ' con espacio no incluye 'From:': el prefijo exacto importa.
        assert len(lineas_que_empiezan(ruta, "From ")) == 2
        assert lineas_que_empiezan(ruta, "Subject:") == ["Subject: prueba"]
        assert lineas_que_empiezan(ruta, "Zzz") == []
def test_promedio() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        ruta = _crear(tmp, MUESTRA)
        assert math.isclose(promedio_confianza(ruta), (0.8475 + 0.6178) / 2)
def test_sin_lineas_de_confianza() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        ruta = _crear(tmp, "From x@y.z\nSubject: nada\n")
        try:
            promedio_confianza(ruta)
        except ValueError:
            return
    raise AssertionError("debió lanzar ValueError: no hay datos que promediar")

if __name__ == "__main__":
    test_filtrar()
    test_promedio()
    test_sin_lineas_de_confianza()
    print("OK: 3 pruebas de ej02_buscar_en_archivo")
