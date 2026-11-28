# Día 10 · Autoevaluación de Matemática (Semana 2)

## 1. Propiedades de logaritmos y cambio de base
1. **Simplificar:** $\frac{\log(3)}{\log_n(3)}$
   * **Solución:** Aplicando cambio de base $\log_n(3) = \frac{\log(3)}{\log(n)}$, al dividir obtenemos **$\log(n)$**.

2. **Evaluar con cambio de base:** $\log_5\left(\frac{1}{1000}\right)$
   * **Solución:** $\frac{\log(10^{-3})}{\log(5)} = \frac{-3}{\log(5)} \approx \mathbf{-4.292}$.

## 2. Ecuaciones exponenciales
3. **Despejar $t$ en base 10:** $2450 = 2000e^{0.1t}$
   * **Solución:**
     $$\frac{49}{40} = e^{0.1t} \implies \log\left(\frac{49}{40}\right) = 0.1t\log(e) \implies t = \frac{10\log\left(\frac{49}{40}\right)}{\log(e)} \approx \mathbf{2.031}$$

4. **Despejar $y$ en base 7:** $5 \cdot 7^{2y} = 175$
   * **Solución:**
     $$7^{2y} = 35 \implies 2y = \log_7(35) \implies y = \frac{\log_7(35)}{2} \approx \mathbf{0.914}$$

5. **Despejar $z$ exacto y aproximado:** $10^{\frac{2z}{3}} = 15$
   * **Solución exacta:** $z = \frac{3\log(15)}{2}$
   * **Aproximación a la milésima:** $z \approx \mathbf{1.764}$

## 3. Log-probabilidades y estabilidad numérica
6. **Producto de probabilidades pequeñas:** $P = 10^{-120} \cdot 10^{-150} \cdot 10^{-80}$
   * **Problema en punto flotante:** En Python ocurre *underflow* y el producto directo da `0.0`.
   * **Solución en escala logarítmica:**
     $$\log_{10}(P) = -120 + (-150) + (-80) = \mathbf{-350}$$

## 4. Sumatorias y conteo de pares (Frontera BPE)
7. **Suma de los primeros $N$ términos:** $\sum_{k=1}^{100} (2k - 1)$
   * **Solución:** La suma de los primeros $n$ impares es $n^2$, por lo tanto $100^2 = \mathbf{10000}$.

8. **Frecuencia de bigramas (BPE):** Para `["robot", "robot", "roba"]`
   * **Conteo de pares:** `{'ro': 3, 'ob': 3, 'bo': 2, 'ot': 2, 'ba': 1}`.
   * **Par más frecuente:** **`'ro'`** (empate con `'ob'` en 3 apariciones; `'ro'` es la primera unión por orden de aparición).
