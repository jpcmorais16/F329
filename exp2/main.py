import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import openpyxl
from scipy import odr

dados = pd.read_excel("planilha.xlsx", "Planilha1")

fQuadrada = dados['frequência'] ** 2
corrente = dados['corrente']


plt.scatter(corrente, fQuadrada)

data = odr.RealData(corrente, fQuadrada)
odreg = odr.ODR(data, odr.models.unilinear)
odreg.set_job(fit_type=2) # muda para mínimos quadrados
ans = odreg.run()


a, b = ans.beta
da, db = ans.sd_beta

print(f'coef. angular = ({a}+-{da})')
print(f'coef. linear = ({b}+-{db})')

rotulo = 'Regressão Linear'


# monta os limites para desenho da reta
X = np.linspace(min(corrente), max(fQuadrada), num=200)
Y = a * X + b
# e faz o gráfico dela atrá dos pontos
plt.plot(X, Y, color='red', alpha=0.4, label=rotulo)
# para exibir as legendas do gráfico
plt.legend()

