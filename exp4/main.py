import numpy as np
from matplotlib import pyplot as plt



def plotCurves(Vp1, Vp2, f, phi,
               rangeT, scaleFactor1, scaleFactor2, rangeTicks,
               namefig, titulo):
    tValues = []

    for i in range(-rangeT, rangeT):
        tValues.append(i / scaleFactor1)

    # Vp = 2
    # f = 100
    # phi = 0

    y1 = []

    for i in range(-rangeT, rangeT):
        y1.append(Vp1 * np.sin(2 * 3.14 * f * tValues[i]))

    plt.plot(tValues, y1)

    y2 = []

    for i in range(-rangeT, rangeT):
        y = Vp2 * np.sin(2 * 3.14 * f * tValues[i] + phi)
        #if(y < 0):
        #    y = 0
        y2.append(y)

    ticks = []
    for i in range(-rangeTicks, rangeTicks):
        ticks.append(100*i / scaleFactor2)

    ticks = [-100 / scaleFactor2, -50 / scaleFactor2, 0, 50 / scaleFactor2, 100 / scaleFactor2]
    plt.plot(tValues, y2)
    #plt.xticks(ticks)
    plt.grid()

    plt.xlabel("Tempo(s)")
    plt.ylabel("Tensão(V)")
    plt.title(titulo)
    plt.savefig(namefig)
    plt.show()


plotCurves(2, 1.760, 100, 3.14,
           150, 10000, 10000, 10,
           "grafico1.png", "Circuito 1")

plotCurves(3.92, 1.64, 100, 146 * 3.14 / 180,
           150, 10000, 10000, 10,
           "grafico2.png", "Circuito 2")







plotCurves(4.04, 0.04, 30,2 * 3.14/3,
           150, 1000, 1000, 10,
           "grafico3.png", "Circuito 3 (30Hz)")

plotCurves(4.12, 0.132, 2998, 2* 3.14 / 3,
           150, 100000, 100000, 10,
           "grafico4.png", "Circuito 3 (3000Hz)")

xValues = []
for i in range(-100, 100):
    xValues.append(.5*i/10000000)


y1 = []
for i in range(-100, 100):
    y1.append(4 * np.sin(2 * 3.14 * 300000 * xValues[i]))

y2 = []
for i in range(-100, 100):
    y2.append(3.4 * np.sin(2 * 3.14 * 300000 * xValues[i]))


plt.plot(xValues, y1)
plt.plot(xValues, y2)
plt.grid()

plt.xlabel("Tempo(s)")
plt.ylabel("Tensão(V)")
plt.title("Circuito 3 (300000Hz)")
plt.savefig("grafico5.png")
plt.show()
