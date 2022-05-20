import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import openpyxl
from scipy import odr
import RegressaoLinear as rL


resistor = pd.read_excel('Dados.xlsx', sheet_name='Resistor')
colunaX = 'Voltímetro (V)'
colunaY = 'Amperímetro (mA)'

x = resistor[colunaX]
y = resistor[colunaY]

plt.scatter(x,y)
plt.plot(x,y)
#plt.axvline(x=0, c="red", label="x=0")
#plt.axhline(y=0, c="yellow", label="y=0")
plt.show()
plt.savefig('grafico.png')


# -----------------------------------------------------
diodomA = pd.read_excel('Dados.xlsx', sheet_name='Diodo (mA)')
diodouA = pd.read_excel('Dados.xlsx', sheet_name='Diodo (microA)')


colunaX = 'Voltímetro (V)'
colunaY = 'Amperímetro'
diodouA[colunaY] = diodouA[colunaY] * 0.001

df = pd.concat([diodomA, diodouA]) # tao com nome de tabelas trocados
df_positivos = df[df[colunaX] > 0]

teste = diodomA[diodomA[colunaX] >= 0]

x = df_positivos[colunaX]
y = df_positivos[colunaY]




plt.scatter(x, y)
plt.plot(x, y)
plt.show()