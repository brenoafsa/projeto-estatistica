from main_info import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

hipotese_nula = 25000

stat, p_value = stats.wilcoxon(mtbf_lista, alternative='two-sided')
print("Estatística do teste U de Mann-Whitney:", stat)
print("Valor-p do teste U de Mann-Whitney:", p_value)

alpha = 0.05
if p_value > alpha:
    print("Aceitamos H0")
else:
    print("Rejeitamos H0")

plt.figure(figsize=(8, 6))
plt.hist(mtbf_lista, bins=10, edgecolor='black', alpha=0.7)
plt.axvline(x=np.mean(mtbf_lista), color='red', linestyle='--', linewidth=1.5, label='Média dos dados')
plt.axvline(x=hipotese_nula, color='blue', linestyle='--', linewidth=1.5, label='Hipótese Nula: 25000 MB/s')
plt.title("Histograma de Transferência de Dados do SSD")
plt.xlabel("Transferência de Dados (MB/s)")
plt.ylabel("Frequência")
plt.legend()
plt.grid(False)
plt.show()