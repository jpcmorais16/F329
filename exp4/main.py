import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import openpyxl
from scipy import odr


def plotCurves(Vp1, Vp2, f, phi,
               rangeT, scaleFactor, rangeTicks,
               namefig):
    tValues = []

    for i in range(-rangeT, rangeT):
        tValues.append(i / scaleFactor)

    # Vp = 2
    # f = 100
    # phi = 0

    y1 = []

    for i in range(-rangeT, rangeT):
        y1.append(Vp1 * np.sin(2 * 3.14 * f * tValues[i]))

    plt.plot(tValues, y1)

    y2 = []

    for i in range(-rangeT, rangeT):
        y2.append(Vp2 * np.sin(2 * 3.14 * f * tValues[i] + phi))

    ticks = []
    for i in range(-rangeTicks, rangeTicks):
        ticks.append(i / scaleFactor)

    ticks = [-100 / scaleFactor, -50 / scaleFactor, 0, 50 / scaleFactor, 100 / scaleFactor]
    plt.plot(tValues, y2)
    plt.xticks(ticks)
    plt.grid()

    plt.savefig(namefig)
    plt.show()


plotCurves(2, 1.760, 100, 3.14,
           150, 10000, 150,
           "grafico1.png")

plotCurves(3.92, 1.64, 100, 146 * 3.14 / 180,
           150, 10000, 150,
           "grafico2.png")

plotCurves(4.12, 0.132, 2998, 3.14 / 2,
           150, 100000, 15,
           "grafico3.png")
