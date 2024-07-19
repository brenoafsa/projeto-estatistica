import plotly.graph_objs as go
import numpy as np
from statsmodels.graphics.gofplots import qqplot



lista1 = []
with open("MTBF.txt", 'r') as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:#laço for para passar os dados entregues numa lista, ja convertendo em float
    lista1.append(float(linha.replace(',', '.')))

def tipdesviop(**par):
    lista = par["lista"]
    tipo = par["tipo"]
    r = desvioPA(lista)
    return r

def mediaA(lista): #calculo da media aritmetica
    soma = 0
    n = len(lista)
    for i in lista:
        soma += i
    total = soma/n
    return total

def calcSQD(lista):#calculo da diferença do quadrado
    med = mediaA(lista)
    soma = 0
    for i in lista:
        soma += (i-med)**2
    return soma

def desvioPA(lista):
    soma = calcSQD(lista)
    n = len(lista)
    total = soma/(n-1)
    desviopa = total**1/2
    return desviopa

t = 0
m1 = tipdesviop(tipo = t, lista = lista1)
print('O desvio padrão amostral é:',m1)
