from main_info import *
import matplotlib.pyplot as plt
from scipy.stats import normaltest, probplot

def normal_hypothesis_test(data):
    stat, p = normaltest(data)
    return stat, p


def qq_plot(data):
    fig, ax = plt.subplots(figsize=(8, 4))
    probplot(data, plot=ax)

    # Definir título e rótulos dos eixos
    ax.set_title("Q-Q plot dos dados")
    ax.set_xlabel("Quantis teóricos")
    ax.set_ylabel("Velocidade Internet")

    return plt.show()

alpha = 0.05
statistic, p_value = normal_hypothesis_test(mtbf_lista)

if p_value > alpha:
    print(f'Há evidências suficientes, ao nível de significância de 5%, para confirmar que os dados são normalmente distribuídos, pois o p-value dos dados é de {p_value:.4f} e é maior que o alpha ({alpha}).')
else:
    print(f'Não há evidências suficientes, ao nível de significância de 5%, para confirmar que os dados são normalmente distribuídos, pois o p-value dos dados é de {p_value:.4f} e é menor que o alpha ({alpha}).')

    qq_plt = qq_plot(mtbf_lista)