import random
import math
import RegressaoLinear as rL
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



def func(name, title, valor, arquivo):
    dados = pd.read_excel("Planilha sem título.xlsx", sheet_name=name)

    df = dados.drop(0)
    df = df.drop(1)
    #print(df)
    time = df["Time (s)"]
    soundPressure = df["Sound pressure level (dB)"]


    a, da, b, db = rL.regLin(time, soundPressure)

    arquivo.write("\n\n" + title + "\n\n")
    arquivo.write("a: {}\n".format(a))
    arquivo.write("da: {}\n".format(da))
    arquivo.write("b: {}\n".format(b))
    arquivo.write("db: {}\n".format(db))

    #print(a, da, b, db)
    #constante = np.log10(np.e)*np.log10(20)/np.log(-a)
    #print(constante)
    #print(constante/valor)

    x = time
    y = a * x + b
    plt.scatter(time, soundPressure)
    plt.yticks([-80, -60, -40, -20, 0])
    plt.grid()
    plt.title(title)
    plt.savefig(title + ".png")
    plt.show()
    plt.clf()

    plt.plot(x, y)
    plt.grid()
    plt.title("Linearização: " + title)
    plt.savefig(title + "reglin.png")
    plt.show()
    plt.clf()


arquivo = open('coeficientes.txt', "w")


func("4.7,1000", "Resistência 4700ohm com um capacitor", 1, arquivo)
func('1,1000', "Resistência de 1000ohm com um capacitor", 1, arquivo)
func('1,2000', "Resistência de 1000ohm com dois capacitores em paralelo", 1, arquivo)
func('10,2000', "Resistência de 10000ohm com dois capacitores em paralelo", 1, arquivo)
func('10,1000', "Resistência de 10000ohm com um capacitor", 1, arquivo)

arquivo.close()