import math

# Problema 1: Decibeles
db = 10 * math.log10(1000)
potencia_diff = 10 ** ((60 - 40) / 10)
print(f"P1: {db} dB | Diferencia: {potencia_diff} veces")

# Problema 2: pH
ph = -math.log10(1e-3)
acidez_diff = 10 ** (7 - 5)
print(f"P2: pH {ph} | Más ácida: {acidez_diff} veces")

# Problema 3: Órdenes de magnitud
ordenes = math.log10(11.8)
print(f"P3: {ordenes:.3f} órdenes")

# Problema 4: Log-probabilidades y Perplejidad
probs = [0.5, 0.25, 0.8]
producto = math.prod(probs)
suma_ln = sum(math.log(p) for p in probs)
nll_promedio = -suma_ln / len(probs)
perplejidad = math.exp(nll_promedio)
print(f"P4: prod={producto:.4f}",
      f"suma_ln={suma_ln:.4f}",
      f"NLL={nll_promedio:.4f}",
      f"PPL={perplejidad:.4f}")

# Problema 5: Underflow vs Log-space
print("P5 (underflow):", 0.1 ** 400)
print("P5 (log-space):", 400 * math.log(0.1))
print(f"P5 log-10={400 * math.log10(0.1):.1f}")

# Problema 6: Separación en eje log10
dist_1 = math.log10(100) - math.log10(10)
dist_2 = math.log10(2000) - math.log10(1000)
print(f"P6: dist(10,100)={dist_1:.4f} vs dist(1000,2000)={dist_2:.4f}")
print("En una escala logaritmica cuenta la razon de los numeros" 
      " por 10 contra por 2, no su diferencia")
