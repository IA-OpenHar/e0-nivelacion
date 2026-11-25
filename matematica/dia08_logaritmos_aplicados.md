# Día 08 - B1: Logaritmos aplicados (escalas log y log-probabilidades)

## Problema 1
- **1000 veces la potencia de referencia:** `10 * log10(1000) = 10 * 3 = 30 dB`.
- **Diferencia entre 60 dB y 40 dB:** Hay 20 dB de diferencia. Como cada 10 dB multiplica la potencia por 10, `10^(20/10) = 10^2 = 100 veces` más potencia.

## Problema 2
- **pH con `[H+] = 10^-3 mol/L`:** `pH = -log10(10^-3) = 3`.
- **pH 5 vs pH 7:** Bajar 2 unidades de pH se multiplica la concentración de `H+` por `10^2 = 100 veces` más ácida.

## Problema 3
- **Órdenes de magnitud de 11.8:** `log10(11.8) ≈ 1.072 órdenes`.

## Problema 4
Probabilidades: `[0.5, 0.25, 0.8]`
- **Producto:** `0.5 * 0.25 * 0.8 = 0.1`
- **Suma de ln:** `ln(0.5) + ln(0.25) + ln(0.8) ≈ -2.3026`
- **NLL promedio:** `-(-2.3026) / 3 ≈ 0.7675`
- **Perplejidad:** `e^(0.7675) ≈ 2.1544`

## Problema 5
- `0.1 ** 400` devuelve `0.0` porque ocurre un **underflow**: el número `10^-400` es menor al mínimo representable en punto flotante de 64 bits (`~4.9 * 10^-324). y Python lo redondea a cero.
- `400 * math.log(0.1)` devuelve `-921.034(logaritmo natural, en base 10 da menos 400)` porque transforma el producto de números diminutos en una suma/multiplicación de logaritmos moderados (`ln(a^b) = b * ln(a)`), evitando perder precisión.

## Problema 6
- **Par (10, 100):** `log10(100) - log10(10) = 2 - 1 = 1.0` unidad.
- **Par (1000, 2000):** `log10(2000) - log10(1000) ≈ 3.301 - 3 = 0.301` unidades.
- **Respuesta:** El par **(10, 100)** queda más separado porque en un eje logarítmico las distancias representan **cocientes** (`100/10 = 10x` frente a `2000/1000 = 2x`), no diferencias absolutas.
