mkdir -p ~/estudio/e0/matematica

cat << 'EOF' > ~/estudio/e0/matematica/dia06_exponenciales.md
# Día 6 - Bloque B1: Funciones exponenciales

## Respuestas Problemas 1–6

1. **Crecimiento / Decaimiento:**
   - $f(x) = 3 \cdot (1.25)^x$: **Crecimiento** del **25%** por periodo.
   - $g(x) = 500 \cdot (0.8)^x$: **Decaimiento** del **20%** por periodo.

2. **Tabla de valores:**
   - Es **exponencial** (cociente constante igual a 3).
   - Fórmula: $y(x) = 4 \cdot 3^x$
   - $y(5) = 972$

3. **Decaimiento del learning rate:**
   - Bloques de $k$ pasos: **10 bloques**.
   - $\text{lr}(10\,000) \approx 0.000665$

4. **Horizonte de tareas (duplicación cada 7 meses):**
   - En 21 meses: **8 horas**.
   - En 28 meses: **16 horas**.
   - Meses para llegar a 8 horas: **21 meses**.

5. **Interés compuesto (1000 soles al 5% por 10 años):**
   - Monto final: **1628.89 soles**.

6. **Exponencial vs. Lineal ($g(x) > f(x)$):**
   - Primer entero: **$x = 10$**.
   - Vecinos:
     - $x = 9 \rightarrow f(9) = 550,\; g(9) = 512$
     - $x = 10 \rightarrow f(10) = 600,\; g(10) = 1024$
     - $x = 11 \rightarrow f(11) = 650,\; g(11) = 2048$
EOF
