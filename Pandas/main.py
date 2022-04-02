import numpy
import pandas as pd
from matplotlib import pyplot as plt
import openpyxl

niveis = [0.5, 1, 1.5, 2, 2.5]

def CurvaDeNivel(tabela, nome, niveis):

    plt.tricontour(tabela['x'], tabela['y'], tabela['V'], niveis, cmap='winter')

    plt.colorbar().set_label("DDP(V)")

    plt.xlabel('X(cm)')
    plt.ylabel('Y(cm)')


    plt.grid(True)

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

niveis = [0.5, 1, 1.5, 2, 2.4]
CurvaDeNivel(paralelo, 'paralelo', niveis)

niveis = [0.5, 1, 1.5, 2]
CurvaDeNivel(ponta, 'ponta', niveis)

niveis = [0.5, 1, 1.25, 1.5, 1.75, 2]
CurvaDeNivel(aro, 'aro', niveis)


