import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import openpyxl
from scipy import odr
import RegressaoLinear as rL


arquivo = open('coeficientes.txt', "w")


# 5.1 ---------------------------------

resistor = pd.read_excel('Dados.xlsx', sheet_name='Resistor')

voltagem = resistor["Voltímetro (V)"]
corrente = resistor['Amperímetro (mA)']
resistencia = resistor["Resistência (ohm)"]

plt.scatter(voltagem, corrente)
plt.plot(voltagem, corrente)
plt.xlabel("Tensão (V)")
plt.ylabel("Corrente (mA)")
plt.show()
plt.savefig('5.1 - corrente-voltagem.png')

plt.scatter(voltagem, resistencia)
plt.plot(voltagem, resistencia)
plt.xlabel("Tensão (V)")
plt.ylabel("Resistência (ohm)")
plt.yticks([0,  20,  40,  60,  80,  100, 120, 140])
plt.show()
plt.savefig('5.1 - resistencia-voltagem.png')

a, da, b, db = rL.regLin(voltagem, corrente)
R = 1000 / a
dR = da * 1000 / (a**2)
print(a, da, b, db)
arquivo.write("corrente x voltagem:\n\n")
arquivo.write("a: {}\n".format(a))
arquivo.write("da: {}\n".format(da))
arquivo.write("b: {}\n".format(b))
arquivo.write("db: {}\n".format(db))
arquivo.write("R: {}\n".format(R))
arquivo.write("dR: {}\n".format(dR))

x = voltagem
y = a * x + b
plt.plot(x, y)
plt.xlabel("Tensão (V)")
plt.ylabel("Corrente (mA)")
plt.show()
plt.savefig("7.1 - RegLin Corrente - Voltagem.png")



# ======================================================


diodo = pd.read_excel('Dados.xlsx', sheet_name='Diodo')
diodo = diodo[diodo['Voltímetro (V)'] > -1]

voltagem = diodo['Voltímetro (V)']
corrente = diodo['Amperímetro']
resistencia = diodo['Resistência (ohm)']
lnResistencia = diodo['lnR']


plt.scatter(voltagem, corrente)
plt.plot(voltagem, corrente)
plt.xlabel("Tensão (V)")
plt.ylabel("Corrente (mA)")
#plt.xticks([-10, -5, 0, 0.5, 1, 1.5])
plt.show()
plt.savefig('3.2 - corrente-voltagem.png')


diodo = pd.read_excel('Planilha.xlsx', sheet_name='Página1')

voltagem = diodo['Voltímetro (V)']
corrente = diodo['Amperímetro']
resistencia = diodo['Resistência (ohm)']
lnResistencia = diodo['lnR']
lnCorrente = diodo['lnI']


plt.scatter(voltagem, resistencia)
plt.plot(voltagem, resistencia)
plt.xlabel("Tensão (V)")
plt.ylabel("Resistência (ohm)")
plt.xscale("log")
plt.yscale("log")
plt.show()
plt.savefig('4.2 - resistencia-voltagem.png')


plt.scatter(voltagem, lnCorrente)
plt.plot(voltagem, lnCorrente)
plt.xlabel("Tensão (V)")
plt.ylabel("Logaritmo Neperiano da Corrente")
#plt.xscale("log")
plt.show()
plt.savefig('8.2 - LNcorrente-voltagem.png')


"""resistor = pd.read_excel('Dados.xlsx', sheet_name='Resistor')
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
plt.show()"""
arquivo.close()