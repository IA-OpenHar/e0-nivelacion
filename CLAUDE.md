# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Qué es este repo

Etapa 0 (nivelación) de un plan de estudios personal de Ingeniería de IA, Ciencia de Datos y Robótica. Son ejercicios de aprendizaje, no un producto: el autor está aprendiendo, así que conviene explicar los cambios y respetar el nivel y el alcance de cada ejercicio. No metas técnicas más avanzadas que las del capítulo en curso salvo que lo pidan.

- `py4e/capNN/`: ejercicios de *Python for Everybody* (`ejNN_*.py`, más `practica/pNN_*.py` en el cap. 5). `cap07/datos/mbox-short.txt` es el archivo de datos del libro.
- `missing/claseNN/`: *The Missing Semester* (MIT): scripts de shell y pipelines (`clase04/pipelines.txt` documenta cada pipeline con su salida esperada sobre `traza_agente.log`).
- `proyectos/`: el mini-proyecto de cada viernes (p. ej. `calculadora/`, CLI con modo argumentos y modo interactivo).
- `robotica/semanaNN/`: física para robótica (unidades, vectores, cinemática, leyes de Newton, tiro parabólico).
- `matematica/`: apuntes en Markdown (`diaNN_*.md`, `bitacora_*.md`) con algún script de apoyo.

Todo el código, los comentarios, los docstrings, los mensajes de error y los mensajes de commit están en **español**.

## Ejecutar y probar

La CI (GitHub Actions) corre `python -m pytest` desde la raíz en cada push. Cada prueba también se puede ejecutar desde su propia carpeta:

```bash
cd robotica/semana02 && python3 test_newton.py      # imprime "OK: N pruebas de ..."
cd py4e/cap07 && python3 test_ej02_buscar_en_archivo.py
python3 proyectos/calculadora/test_calculadora.py   # el sys.path incluye la carpeta del script, así que funciona desde la raíz
```

Los `test_*.py` definen funciones `test_*()` (compatibles con pytest) y un bloque `if __name__ == "__main__":` que las llama una por una y termina con un `print("OK: ...")`. Si agregas una prueba nueva, agrégala también a ese bloque. Para ejecutar una sola prueba: `cd <carpeta> && python3 -c "import test_x; test_x.test_nombre()"`, o con pytest `pytest test_x.py::test_nombre`.

El entorno virtual `.venv` está en la carpeta padre (`estudio/.venv`, fuera del repositorio).

Los ejercicios más antiguos (p. ej. `proyectos/calculadora/test_calculadora.py`, `py4e/cap04/ej08_*.py`) llevan sus asserts directamente en `if __name__ == '__main__':` y terminan con `print('Todas las pruebas pasan')`.

## Convenciones de código

- PEP 8 (los commits recientes corrigieron el formato), anotaciones de tipo y docstrings en español en cada función.
- Las entradas inválidas lanzan `ValueError` con un mensaje en español. Las pruebas comprueban los errores con `try/except ... continue` seguido de `raise AssertionError(...)`, o con un helper `debe_fallar`, no con `pytest.raises`.
- Los floats se comparan con `math.isclose` (con `abs_tol` cuando se compara contra 0).
- Los archivos se abren con `encoding="utf-8"`. Las pruebas que leen archivos crean sus datos con `tempfile` en lugar de depender de `datos/`.
- Al principio del módulo van constantes en MAYÚSCULAS (p. ej. `OPERADORES` como tupla inmutable, `PREFIJO_CONFIANZA`).

## Git

Una sola rama, `main`, que sigue a `origin/main`. Hay ramas de práctica que ya se fusionaron (p. ej. `practica/divergente`). `.gitignore` excluye `*.log` y `*.zip`, con una excepción explícita para `missing/clase04/traza_agente.log`, que se versiona porque los pipelines dependen de él.

## Cómo colaborar

- **Rol de Claude:** el autor está aprendiendo. Claude actúa como maestro y guía: explica, señala errores y propone pistas, pero **no escribe ni edita código directamente** por el autor.
- **Estilo de código:** Todo archivo Python debe cumplir con `pycodestyle` (máximo 79 caracteres por línea y sin espacios extra en cortes como `texto[inicio:]`).
- **Pruebas antes de subir:** Ejecutar `python -m pytest` desde la raíz y confirmar que pasen antes de hacer `git push`.
- **Mensajes de commit:** Usar mensajes cortos (máximo 50 caracteres), claros, con tildes y un commit por cada cambio.
- **Entorno virtual:** Se utiliza un único entorno virtual `.venv` ubicado en la carpeta padre (`estudio/.venv`, fuera del repositorio).
