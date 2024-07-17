import statistics
import numpy as np
from scipy.stats import kurtosis

def extrair_numeros(caminho):
    mtbf_numeros = []
    with open(caminho, 'r') as arquivo:
        for line in arquivo:
            numero = float(line.strip().replace(',', '.'))
            mtbf_numeros.append(numero)
    return mtbf_numeros

def maior_valor(data):
    return max(data)

def menor_valor(data):
    return min(data)

def definir_media(data):
    return round(statistics.mean(data), 2)

def definir_mediana(data):
    return round(statistics.median(data), 2)

def definir_moda(data):
    return round(statistics.mode(data), 2)

def definir_desvio_padrao(data):
    return round(statistics.stdev(data), 2)

def definir_variancia(data):
    return round(statistics.variance(data), 2)

def definir_coeficiente_variancao(desvio, med):
    return  round(desvio / med, 2)

def definir_quartis(data):
    return np.percentile(data, [25, 50, 75, 100])

def definir_curtose(data):
    return round(kurtosis(data), 2) 

#Define a lista
mtbf_lista = extrair_numeros('documents\MTBF.txt')

#Maior e Menor valor
max = maior_valor(mtbf_lista)
min = menor_valor(mtbf_lista)

#Media, Mediana e Moda
media = definir_media(mtbf_lista)
mediana = definir_mediana(mtbf_lista)
moda = definir_moda(mtbf_lista)

#Desvio Padrão e Variância
dp = definir_desvio_padrao(mtbf_lista)
var = definir_variancia(mtbf_lista)

#Cof. Var e Quartis
cof_var = definir_coeficiente_variancao(dp, media)
quartis = definir_quartis(mtbf_lista)

#Curtose
curtose = definir_curtose(mtbf_lista)

print(f"Maior valor: {max}, Menor Valor: {min}, Media: {media}, Mediana: {mediana}, Moda: {moda}, Desvio Padrão: {dp}, Variância: {var}, Coeficiente de Variância: {cof_var}, Quartis: {quartis}, Curtose: {curtose}")