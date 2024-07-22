from main_info import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

media = np.mean(mtbf_lista)
desvio_padrao = np.std(mtbf_lista)

xmin = np.min(mtbf_lista) - 1
xmax = np.max(mtbf_lista) + 1
x = np.linspace(xmin, xmax, 100)
y = norm.pdf(x, media, desvio_padrao)

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'r-', linewidth=2, label='Distribuição Normal')

alpha = 0.05 
z_alpha = norm.ppf(1 - alpha / 2, media, desvio_padrao)
plt.fill_between(x, 0, y, where=(x >= z_alpha), color='red', alpha=0.3, label=f'Área de alpha ({alpha})')

plt.title('Gráfico de Distribuição Normal com Área de Alpha')
plt.xlabel('Valores')
plt.ylabel('Densidade de Probabilidade')
plt.axvline(media, color='g', linestyle='dashed', linewidth=1, label=f'Média = {media:.2f}')
plt.legend()
plt.text(xmax - 1, np.max(y) - 0.02, f'Desvio Padrão = {desvio_padrao:.2f}', fontsize=10, color='purple', ha='right')

plt.grid(True)
plt.show()
