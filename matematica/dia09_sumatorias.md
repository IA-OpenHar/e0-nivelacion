# Día 9 (B1): Notación de sumatoria $\Sigma$ y productoria $\Pi$

## Problema 1: Sumatorias básicas

1. **Cálculo de $\sum_{i=1}^{5} i$:**
   $$\sum_{i=1}^{5} i = 1 + 2 + 3 + 4 + 5 = 15$$

2. **Cálculo de $\sum_{i=1}^{4} i^2$:**
   $$\sum_{i=1}^{4} i^2 = 1^2 + 2^2 + 3^2 + 4^2 = 1 + 4 + 9 + 16 = 30$$

---

## Problema 2: Fórmula de Gauss y series aritméticas

1. **Suma del $1$ al $100$ usando la fórmula de Gauss $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$:**
   $$\sum_{i=1}^{100} i = \frac{100 \times 101}{2} = 5050$$

2. **Cálculo de $\sum_{k=1}^{550} (2k + 50)$ separando en dos sumas:**
   $$\sum_{k=1}^{550} (2k + 50) = 2\sum_{k=1}^{550} k + \sum_{k=1}^{550} 50$$

   * **Primera suma (Gauss con $n = 550$):**
     $$2 \times \left(\frac{550 \times 551}{2}\right) = 550 \times 551 = 303\,050$$

   * **Segunda suma (constante $50$ repetida $550$ veces):**
     $$550 \times 50 = 27\,500$$

   * **Resultado total:**
     $$303\,050 + 27\,500 = 330\,550$$

---

## Problema 3: Productoria ($\Pi$) y logaritmos

1. **Cálculo de $\prod_{i=1}^{5} i$:**
   $$\prod_{i=1}^{5} i = 1 \times 2 \times 3 \times 4 \times 5 = 120$$

2. **Productoria de las probabilidades $p = [0.5, 0.25, 0.8]$:**
   $$\Pi = 0.5 \times 0.25 \times 0.8 = 0.1$$

3. **Comprobación de $\ln \Pi = \sum \ln p_i$:**
   * **Logaritmo del producto:** $\ln(0.1) \approx -2.3026$
   * **Suma de logaritmos:** $\ln(0.5) + \ln(0.25) + \ln(0.8) \approx -0.6931 - 1.3863 - 0.2231 = -2.3026$
   * **Conclusión:** Ambos lados son iguales ($-2.3026$).

---

## Problema 4: Media y Error Cuadrático Medio (MSE)

1. **Media de $x = [2, 4, 9]$ ($n = 3$):**
   $$\bar{x} = \frac{1}{3} \sum_{i=1}^{3} x_i = \frac{2 + 4 + 9}{3} = \frac{15}{3} = 5$$

2. **MSE entre $y = [3, 5]$ y $\hat{y} = [2.5, 5.5]$ ($n = 2$):**
   $$\text{MSE} = \frac{1}{2} \sum_{i=1}^{2} (y_i - \hat{y}_i)^2 = \frac{(3 - 2.5)^2 + (5 - 5.5)^2}{2} = \frac{0.25 + 0.25}{2} = 0.25$$

---

## Problema 5: Multiplicación de matrices

1. **Expresión de $c_{23}$ en $C = A \cdot B$ para matrices $3 \times 3$:**
   $$c_{23} = \sum_{k=1}^{3} a_{2k} \cdot b_{k3} = a_{21}b_{13} + a_{22}b_{23} + a_{23}b_{33}$$

2. **Multiplicaciones necesarias para dos matrices $1000 \times 1000$ (método directo):**
   $$\text{Total de multiplicaciones} = n^3 = 1000^3 = 10^9 \text{ (mil millones de multiplicaciones)}$$

---

## Problema 6: Comprobación en Python

Comandos ejecutados en la terminal para verificar los problemas 2 y 3:

```bash
# Suma de Gauss del 1 al 100 (Problema 2)
python3 -c "print(sum(range(1, 101)))"
# Salida: 5050

# Serie aritmética del 1 al 550 (Problema 2)
python3 -c "print(sum(2*k + 50 for k in range(1, 551)))"
# Salida: 330550

# Productoria del 1 al 5 (Problema 3)
python3 -c "import math; print(math.prod(range(1, 6)))"
# Salida: 120

# Comprobación de probabilidades y logaritmos (Problema 3)
python3 -c "import math; p=[0.5, 0.25, 0.8]; prod=math.prod(p); print(prod, round(math.log(prod), 4), round(sum(math.log(x) for x in p), 4))"
# Salida: 0.1 -2.3026 -2.3026
```
