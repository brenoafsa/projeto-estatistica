from main_info import *
import math
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x_bar = media
u = 70
std = dp
n = 1000
alpha = 0.05

# tipos possíveis: "right-tailed, left-tailed, two-tailed"
tail_hypothesis_type = "right-tailed"

if tail_hypothesis_type == "left-tailed":
    critical_value = stats.norm.ppf(alpha)
elif tail_hypothesis_type == "right-tailed":
    critical_value = stats.norm.ppf(1 - alpha)
else:
    critical_value = stats.norm.ppf(alpha/2)


print("One-Sample", tail_hypothesis_type, "Z-test of true mean")
print("--------------------------------------------------------------------------------------")

if n >= 30:
    print("Tamanho da Amostra >= 30, CLT ")
    z_score = (x_bar - u)/(std/math.sqrt(n))
    critical_value = stats.norm.ppf(alpha)
    
    conclusion = "Falha ao rejeitar a hipótese nula"
    if tail_hypothesis_type == "left-tailed":
        if z_score < critical_value:
            conclusion = "Hipótese Nula foi rejeitada"
    elif tail_hypothesis_type == "right-tailed":
        critical_value = abs(critical_value)
        if z_score > critical_value:
            conclusion = "Hipótese Nula foi rejeitada"
    else:
        z_score = abs(z_score) 
        critical_value = abs(critical_value)
        if z_score > critical_value:
            conclusion = "Hipótese Nula foi rejeitada"

    print("z-score is:", z_score, " and critical value is:", critical_value)
    print(conclusion)
else:
    print("CLT não foi satisfeita")

mu = 70
sigma = dp

x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

y = norm.pdf(x, mu, sigma)

plt.plot(x, y)

plt.xlim(mu - 3*sigma, mu + 3*sigma)

x1 = np.linspace(mu + 3*sigma, -1.645*sigma, 100)
x2 = np.linspace(79.62, 1.645*sigma, 100)
y1 = norm.pdf(x1, mu, sigma)
y2 = norm.pdf(x2, mu, sigma)
plt.fill_between(x1, y1, color='red', alpha=.3)
plt.fill_between(x2, y2, color='white', alpha=1)

plt.title('Distribuição Normal')

plt.show()