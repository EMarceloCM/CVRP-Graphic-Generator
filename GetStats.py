import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Substitua pelos seus 5 tempos (s) e 5 distâncias (km)
tempos = [2691, 2621, 2477, 2321, 2539]
distancias = [874.84, 945.38, 873.28, 857.57, 824.07]

# Cálculo de estatísticas
media_t = np.mean(tempos)
dp_t    = np.std(tempos, ddof=1)
min_t   = np.min(tempos)
max_t   = np.max(tempos)

media_d = np.mean(distancias)
dp_d    = np.std(distancias, ddof=1)
min_d   = np.min(distancias)
max_d   = np.max(distancias)

# DataFrame consolidado
stats = {
    'Métrica': ['Média', 'Desvio Padrão', 'Melhor (mínimo)', 'Pior (máximo)'],
    'Tempo (ms)':    [media_t, dp_t, min_t, max_t],
    'Distância (arbitrária)': [media_d, dp_d, min_d, max_d],
}
df = pd.DataFrame(stats)

# Imprime tabela
print("\n=== Estatísticas Consolidadas ===")
print(df.to_string(index=False, float_format='{:0.4f}'.format))

# Gráfico de barras agrupadas com labels externos
labels = df['Métrica']
values_t = df['Tempo (ms)']
values_d = df['Distância (arbitrária)']
x = np.arange(len(labels))
width = 0.35

plt.figure(figsize=(9, 6))
bars_t = plt.bar(x - width/2, values_t, width, label='Tempo (ms)')
bars_d = plt.bar(x + width/2, values_d, width, label='Distância (arbitrária)')

# Adiciona valores sobre cada barra
for bar in bars_t:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height:.4f}', 
             ha='center', va='bottom')
for bar in bars_d:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height:.4f}', 
             ha='center', va='bottom')

plt.xticks(x, labels)
plt.ylabel('Valor')
plt.title('Comparação das Estatísticas Tempo × Distância (com valores)')

# Aqui posicionamos a legenda *fora* do gráfico, abaixo, centralizada à direita:
plt.legend(
    loc='upper center', 
    bbox_to_anchor=(0.88, -0.05),  # 75% da largura à direita, 15% para baixo do eixo
    ncol=1
)

plt.tight_layout()
plt.show()
