import sympy
import numpy as np
import matplotlib.pyplot as plt

# Configuração Inicial e Variáveis Simbólicas


# Variável simbólica de tempo t (em horas, para uma tempestade de 0 a 6h)
t = sympy.Symbol('t')

# intensidade da chuva (mm/h)
chuva_r = -2*t**2 + 12*t

# Constante de capacidade de drenagem/escoamento urbano (em mm/h)
escoamento = 8

# indicando a velocidade instantânea (em mm/h) com que o nível da água sobe ou desce.
taxa_subida = chuva_r - escoamento


# Acúmulo de Água (Conceito de Integral)
nivel_h = sympy.integrate(taxa_subida, t)
limite_transbordamento = 10


solucoes = sympy.solve(sympy.Eq(nivel_h, limite_transbordamento), t)
tempos_reais_positivos = sorted([
    float(sol.evalf(chop=True))
    for sol in solucoes
    if sol.evalf(chop=True).is_real and float(sol.evalf(chop=True)) > 0
])
t_critico = tempos_reais_positivos[0]


# Saida de Resultados
print("\n--- SAFESLOPE: Previsão de Enchentes ---")
print(f"Intensidade da chuva: {chuva_r} mm/h")
print(f"A água está a subir a: {taxa_subida} mm/h")
print(f"Nível total acumulado: {nivel_h} mm")
print("----------------------------------------")
print(f"ALERTA CRÍTICO: Risco de transbordamento! O limite de {limite_transbordamento}mm será atingido em {t_critico:.2f} horas.")
print("\n")
