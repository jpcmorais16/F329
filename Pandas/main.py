import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import openpyxl
from matplotlib.tri import Triangulation, CubicTriInterpolator


def Potencial(x, y, tabela):
    aux1 = tabela[tabela['x'] == x]
    aux2 = aux1[tabela['y'] == y]
    return aux2['V']


def CurvaDeNivel(tabela, nome, niveis):
    jonas = plt.tricontourf(tabela['x'], tabela['y'], tabela['V'], niveis, cmap='winter')

    print(jonas.collections)

    plt.colorbar().set_label("DDP(V)")

    plt.xlabel('X(cm)')
    plt.ylabel('Y(cm)')

    plt.grid(True)

    triang = Triangulation(tabela['x'], tabela['y'])


    tci = CubicTriInterpolator(triang, -tabela['V'])

    (Ex, Ey) = tci.gradient(triang.x, triang.y)
    E_norm = np.sqrt(Ex ** 2 + Ey ** 2)

    plt.quiver(triang.x, triang.y, Ex / E_norm, Ey / E_norm)

    plt.savefig(nome + '.png')
    plt.show()
    plt.clf()


paralelo = pd.read_excel("planilha.xlsx", "Planilha1")
ponta = pd.read_excel("planilha.xlsx", "Planilha2")
aro = pd.read_excel("planilha.xlsx", "Planilha3")

# ------------------- GRÁFICO -------------------------

paraleloX = paralelo[paralelo['x'] == 0]
aroX = aro[aro['x'] == 0]
pontaX = ponta[ponta['x'] == 0]

plt.scatter(paraleloX['y'], paraleloX['V'], color='red')
plt.plot(paraleloX['y'], paraleloX['V'], color='red', alpha=0.6, label='Placas Paralelas')

plt.plot(pontaX['y'], pontaX['V'], label='Ponta')
plt.scatter(pontaX['y'], pontaX['V'])

plt.plot(aroX['y'], aroX['V'], label='Aro')
plt.scatter(aroX['y'], aroX['V'])

plt.legend()
plt.xlabel('Y(cm)')
plt.ylabel('Diferença de potencial(v)')
plt.title('Diferença de potencial vs Coordenada Y')

plt.grid(True)

plt.savefig('grafico.png')
plt.show()
plt.clf()

# ----------------------- CURVAS DE NIVEL ---------------------------

niveis = []

for y in range(1, 19, 2):
    paraleloY = paralelo[paralelo['y'] == y]
    print(paraleloY)
    niveis.append(paraleloY['V'].mean())
    print(niveis)

niveis.append(0)
niveis.reverse()
niveis.append(2.534545454545454)
CurvaDeNivel(paralelo, 'paralelo', niveis)

CurvaDeNivel(ponta, 'ponta', niveis)

CurvaDeNivel(aro, 'aro', niveis)
