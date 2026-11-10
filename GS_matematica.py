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


# Menu Interativo 
f_nivel_padrao = sympy.lambdify(t, nivel_h, 'numpy')
tempo = np.linspace(0, 6, 300)
nivel_padrao_mm = f_nivel_padrao(tempo)

print("--- MENU INTERATIVO DE SIMULAÇÃO ---")
print("1 - Gerar gráfico com os valores padrão (Escoamento = 8 mm/h, Limite = 10 mm)")
print("2 - Definir novos valores e comparar mudança no gráfico")
opcao = input("Escolha uma opção (1 ou 2) [Enter = 1]: ").strip()

if opcao == "2":
    novo_esc = input("Digite a nova capacidade de escoamento (mm/h) [padrão = 8]: ").strip().replace(",", ".")
    if novo_esc:
        escoamento = float(novo_esc)

    novo_lim = input("Digite o novo limite de transbordamento (mm) [padrão = 10]: ").strip().replace(",", ".")
    if novo_lim:
        limite_transbordamento = float(novo_lim)

    # Recalcula derivada, integral e tempo crítico com os novos valores
    taxa_subida = chuva_r - escoamento
    nivel_h = sympy.integrate(taxa_subida, t)
    solucoes_novas = sympy.solve(sympy.Eq(nivel_h, limite_transbordamento), t)
    tempos_novos = sorted([
        float(sol.evalf(chop=True))
        for sol in solucoes_novas
        if sol.evalf(chop=True).is_real and 0 < float(sol.evalf(chop=True)) <= 6
    ])
    t_critico = tempos_novos[0] if tempos_novos else None

    t_ref = t_critico if t_critico is not None else 3.0
    print(f"\n--- Valores Atualizados (em t = {t_ref:.2f} h) ---")
    print(f"Intensidade da chuva : {float(chuva_r.subs(t, t_ref)):.2f} mm/h")
    print(f"Taxa de subida       : {float(taxa_subida.subs(t, t_ref)):.2f} mm/h")
    print(f"Nível acumulado      : {float(nivel_h.subs(t, t_ref)):.2f} mm")
    if t_critico is not None:
        print(f"NOVO ALERTA: O limite de {limite_transbordamento:.1f} mm será atingido em {t_critico:.2f} horas!\n")
    else:
        print(f"SITUAÇÃO SEGURA: O limite de {limite_transbordamento:.1f} mm não será atingido.\n")

f_nivel_h = sympy.lambdify(t, nivel_h, 'numpy')
nivel_agua_mm = f_nivel_h(tempo)

plt.figure(figsize=(10, 6))

if opcao == "2":
    plt.plot(
        tempo,
        nivel_padrao_mm,
        label='Cenário Padrão (Escoamento = 8 mm/h)',
        color='gray',
        linestyle='-.',
        linewidth=1.8,
        alpha=0.7
    )

plt.plot(
    tempo,
    nivel_agua_mm,
    label=f'Nível de Água Acumulado h(t) (Escoamento = {escoamento} mm/h)',
    color='royalblue',
    linewidth=2.5
)
plt.axhline(
    y=limite_transbordamento,
    color='red',
    linestyle='--',
    linewidth=2,
    label=f'Limite de Transbordamento ({limite_transbordamento} mm)'
)

if t_critico is not None:
    plt.axvline(
        x=t_critico,
        color='darkorange',
        linestyle=':',
        linewidth=2,
        label=f'Tempo Crítico (t ≈ {t_critico:.2f} h)'
    )
    plt.scatter([t_critico], [limite_transbordamento], color='red', zorder=5)

plt.title('Previsão de Acúmulo de Água e Alerta de Enchente')
plt.xlabel('Tempo (horas)')
plt.ylabel('Nível de Água Acumulado (mm)')
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
