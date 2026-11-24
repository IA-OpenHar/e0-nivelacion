# ==========================================
# PROBLEMA 1: Crecimiento o decaimiento
# ==========================================
# f(x) = 3 * (1.25)^x  -> base b = 1.25 (> 1, crecimiento)
# g(x) = 500 * (0.8)^x -> base b = 0.8  (0 < b < 1, decaimiento)

b_f = 1.25
porcentaje_f = (b_f - 1) * 100

b_g = 0.8
porcentaje_g = (1 - b_g) * 100

print("--- Problema 1 ---")
print(f"f(x): Crecimiento del {porcentaje_f:.0f}% por periodo.")
print(f"g(x): Decaimiento del {porcentaje_g:.0f}% por periodo.\n")


# ==========================================
# PROBLEMA 2: Tabla de valores
# ==========================================
# x = 0, 1, 2, 3 -> y = 4, 12, 36, 108
y_vals = [4, 12, 36, 108]

# Verificamos cocientes: y(x+1) / y(x)
cocientes = [y_vals[i+1] / y_vals[i] for i in range(len(y_vals) - 1)]
# Como todos los cocientes son 3, es exponencial: y(x) = a * b^x
a = y_vals[0]  # valor inicial cuando x = 0 -> 4
b = cocientes[0]  # factor constante -> 3

y_5 = a * (b ** 5)

print("--- Problema 2 ---")
print(f"Cocientes: {cocientes} -> Es exponencial.")
print(f"Fórmula: y(x) = {a} * ({int(b)}^x)")
print(f"y(5) = {int(y_5)}\n")


# ==========================================
# PROBLEMA 3: Decaimiento del learning rate
# ==========================================
# Fórmula: lr(paso) = lr_0 * d^(paso / k)
lr_0 = 0.001
d = 0.96
k = 1000
paso = 10000

bloques_k = paso / k
lr_final = lr_0 * (d ** bloques_k)

print("--- Problema 3 ---")
print(f"Bloques de k pasos: {int(bloques_k)} bloques")
print(f"lr en el paso 10 000: {lr_final:.6f}\n")


# ==========================================
# PROBLEMA 4: Horizonte de tareas (Tiempo de duplicación)
# ==========================================
# Fórmula: f(t) = a * 2^(t / T)
# a = 1 hora, T = 7 meses
a_horas = 1
T = 7

# a) ¿Cuánto vale en 21 meses?
val_21 = a_horas * (2 ** (21 / T))

# b) ¿Cuánto vale en 28 meses?
val_28 = a_horas * (2 ** (28 / T))

# c) ¿Cuántos meses hacen falta para llegar a 8 horas?
# 8 = 1 * 2^(t / 7) -> 2^3 = 2^(t / 7) -> t / 7 = 3 -> t = 21
meses_para_8h = 0
while a_horas * (2 ** (meses_para_8h / T)) < 8:
    meses_para_8h += 1

print("--- Problema 4 ---")
print(f"En 21 meses: {int(val_21)} horas")
print(f"En 28 meses: {int(val_28)} horas")
print(f"Meses para llegar a 8 horas: {meses_para_8h} meses\n")


# ==========================================
# PROBLEMA 5: Interés compuesto
# ==========================================
# 1000 soles al 5% anual compuesto durante 10 años
capital = 1000
tasa = 0.05
anios = 10

monto_final = capital * ((1 + tasa) ** anios)

print("--- Problema 5 ---")
print(f"Monto final tras 10 años: {monto_final:.2f} soles\n")


# ==========================================
# PROBLEMA 6: Exponencial vs Lineal
# ==========================================
# f(x) = 100 + 50x  (lineal)
# g(x) = 2^x        (exponencial)
def f(x):
    return 100 + 50 * x

def g(x):
    return 2 ** x

n = 0
while g(n) <= f(n):
    n += 1

print("--- Problema 6 ---")
print(f"Primer entero x >= 0 donde g(x) > f(x): x = {n}")
print("Verificación con vecinos:")
for v in [n - 1, n, n + 1]:
    print(f"  x = {v} -> f({v}) = {f(v)}, g({v}) = {g(v)}")
