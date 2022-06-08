import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import openpyxl
from scipy import odr
import RegressaoLinear as rL

dados = pd.read_excel('Dados_exp_2.xlsx', sheet_name='Planilha1')

colunaX = 'Corrente (mA)'
colunaY = 'f2'

x = dados[colunaX]
y = dados[colunaY]

plt.xlabel('Corrente (mA)')
plt.ylabel('Frequência ao Quadrado (Hz^2)')

plt.xticks([-250, -200, -150, -100, -75, -50, -25, 0, 25, 50, 75, 100, 150, 200, 250])

plt.scatter(x, y)
plt.savefig('Grafico.png')
#plt.show()
plt.clf()

# --------------------------------------------------------------------------------------


positivos = dados[dados[colunaX] >= -11.58]
x = positivos[colunaX]
y = positivos[colunaY]

a, da, b, db = rL.regLin(x, y)
print(a, da, b, db)

X = x
Y = a * X + b
# --------------------------------------------------------------------------------------

negativos = dados[dados[colunaX] < -11.58]
w = negativos[colunaX]
z = negativos[colunaY]

c, dc, d, dd = rL.regLin(w, z)

print(c, dc, d, dd)


W = w
Z = c * W + d

t = plt.plot(X, Y, color='red', alpha=0.4)
plt.plot(W, Z, color='red', alpha=0.4)

plt.scatter(w, z, color='blue')
plt.scatter(x, y, color='blue')

plt.grid()
plt.xticks([-240, -200, -150, -100,  -50,  0,  50,  100, 150, 200, 240])
plt.yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])

plt.xlabel('Corrente (mA)')
plt.ylabel('Frequência ao Quadrado (Hz^2)')
plt.title('Frequência ao quadrado x Corrente')


plt.savefig('Grafico.png')
plt.show()
