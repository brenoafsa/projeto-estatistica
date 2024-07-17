from main_info import *
import matplotlib.pyplot as plt 
import seaborn as sns
import matplotlib.pyplot as plt

def get_boxplot(data):
    plt.boxplot(data)
    plt.title("Testando código")
    plt.ylabel("Banda Larga")
    return plt.show()

def get_histograma(data):
    ax = sns.histplot(data, kde=True)
    ax.set(title="Velocidade Internet em MB X Frequência", xlabel="Velocidade", ylabel="Frequência")
    return plt.show()

def get_linechart(data):
    x = []
    for i in range(len(data)):
        x.append(i*5)
    plt.plot(x, data, linewidth=0.9)
    plt.title("Gráfico temporal da Velocidade de Internet")
    plt.xlabel('Tempo (s)')
    plt.ylabel('Velocidade')
    return plt.show()

box_plot = get_boxplot(mtbf_lista)
histogram = get_histograma(mtbf_lista)
linear_chart = get_linechart(mtbf_lista)