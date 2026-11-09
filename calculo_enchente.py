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
