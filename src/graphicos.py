from main_info import *
import matplotlib.pyplot as plt 
import seaborn as sns

def get_boxplot(data):
    plt.boxplot(data)
    plt.title("Transferência de Dados do SSD")
    plt.ylabel("Velocidade (Mb/s)")
    return plt.show()

def get_histograma(data):
    ax = sns.histplot(data, kde=True)
    ax.set(title="Transferência de Dados do SSD X Frequência", xlabel="Velocidade (Mb/s)", ylabel="Frequência")
    return plt.show()

def get_linechart(data):
    x = []
    for i in range(len(data)):
        x.append(i*5)
    plt.plot(x, data, linewidth=0.9)
    plt.title("Gráfico temporal do Desempenho da transferência de dados do SSD")
    plt.xlabel('Tempo (s)')
    plt.ylabel('Velocidade (Mb)')
    return plt.show()

box_plot = get_boxplot(mtbf_lista)
histogram = get_histograma(mtbf_lista)
linear_chart = get_linechart(mtbf_lista)