import numpy as np
from matplotlib import pyplot as plt
from scipy import odr


def regLin(x, y):
    data = odr.RealData(x, y)
    odreg = odr.ODR(data, odr.models.unilinear)
    odreg.set_job(fit_type=2)
    ans = odreg.run()

    a, b = ans.beta
    da, db = ans.sd_beta

    return a, da, b, db



def regLinPlot(x, y, nomeArquivoGrafico, xLabel, yLabel, Title):
    data = odr.RealData(x, y)
    odreg = odr.ODR(data, odr.models.unilinear)
    odreg.set_job(fit_type=2)  # muda para mínimos quadrados
    ans = odreg.run()

    a, b = ans.beta
    da, db = ans.sd_beta

    print(f'coef. angular = ({a}+-{da})')
    print(f'coef. linear = ({b}+-{db})')


    X = np.linspace(min(x), max(x))
    Y = a * X + b

    plt.plot(X, Y, color='red', alpha=0.4)

    plt.legend()

    plt.scatter(x, y)

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(Title)

    plt.savefig(nomeArquivoGrafico)

    plt.show()
    return a, da, b, db