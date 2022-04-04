import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import openpyxl
from matplotlib.tri import Triangulation, CubicTriInterpolator

def CurvaDeNivel(tabela, nome, niveis, titulo):
    plt.tricontourf(tabela['x'], tabela['y'], tabela['V'], niveis)


    plt.colorbar().set_label("DDP(V)")

    plt.xlabel('X(cm)')
    plt.ylabel('Y(cm)')
    plt.title(titulo)

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
niveis.append(2.534545454545454)


for y in range(1, 19, 2):
    paraleloY = paralelo[paralelo['y'] == y]
    print(paraleloY)
    niveis.append(paraleloY['V'].mean())
    print(niveis)

niveis.append(0)
niveis.reverse()

print(len(niveis))
CurvaDeNivel(paralelo, 'paralelo', niveis, "Placas Paralelas")

CurvaDeNivel(ponta, 'ponta', niveis, "Ponta")

niveisAro = [2.53, 2.3435454545454544,  2.075909090909091,
              1.7, 1.389, 1.24909090909091,  0.95,
             0.5890909090909091, 0.3, 0]

niveisAro.reverse()


CurvaDeNivel(aro, 'aro', niveisAro, "Aro")
