import random
import math
import RegressaoLinear as rL
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



def func(sheetName, title, valor):
    dados = pd.read_excel("Projeto_ind.xlsx", sheet_name=sheetName)

    df = dados.drop(0)
    #print(df)
    time = df["Time (s)"]
    soundPressure = df["Sound pressure level (dB)"]

    for i in range(1, time.size):
        time[i] += random.randrange(-10000000, 10000000)/1000000000
        soundPressure[i] += random.randrange(-10000000, 10000000)/1000000000
        #print(time[i])

    a, da, b, db = rL.regLin(time, soundPressure)
    constante = -20/(a*np.log(10))

    arquivo.write("\n\n" + title + "\n\n")
    arquivo.write("a: {}\n".format(a))
    arquivo.write("da: {}\n".format(da))
    arquivo.write("b: {}\n".format(b))
    arquivo.write("db: {}\n".format(db))
    arquivo.write("constante: {}\n".format(constante))

    x = time
    y = a * x + b
    plt.scatter(time, soundPressure)
    plt.yticks([-80, -60, -40, -20, 0])
    plt.grid()
    plt.title(title)
    #plt.savefig(title + ".png")
    plt.show()
    plt.clf()

    plt.plot(x, y)
    plt.grid()
    plt.title(title)
    #plt.savefig(title + "reglin.png")
    plt.show()
    plt.clf()


arquivo = open('coeficientes2.txt', "w")


func("Circ 1K","Circ 1K", 1000 + 518)
func("Circ 1K série","Circ 1K série", 1000 + 518)
func("Circ 4.7K", "Circ 4.7K", 4700 + 518)
func("Circ 10K", "Circ 10K", 10000 + 518)
func("Circ 10K série", "Circ 10K série", 10000 + 518)

arquivo.close()
