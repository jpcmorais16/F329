import numpy as np;
import pandas as pd;
from matplotlib import pyplot as plt;
import openpyxl;
from matplotlib.patches import FancyArrowPatch

""""%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

feature_x = np.arange(-50, 50, 2)
feature_y = np.arange(-50, 50, 3)

# Creating 2-D grid of features
[X, Y] = np.meshgrid(feature_x, feature_y)

fig, ax = plt.subplots(1, 1)

z = 0.5*np.array((Y-X)*(Y-X) + 0.5*(1-X)*(1-X))

# plots contour lines
ax.contour(X, Y, z, 10, cmap = 'jet')
ax.grid(True)
ax.axis('scaled')
#ax.clabel(cp, inline=1, fontsize=10)
ax.set_title('Contour Plot')
ax.set_xlabel('feature_x')
ax.set_ylabel('feature_y')

plt.show()"""

paralelo = pd.read_excel("planilha.xlsx", "Planilha1")

feature_x = paralelo['x']
feature_y = paralelo['y']

x, y = np.meshgrid(feature_x, feature_y)
z = 0.5*(y-x)**2 + 0.5*(1-x)**2
u = 2*x - y - 1
v = y - x

# Normalize all gradients to focus on the direction not the magnitude
norm = np.linalg.norm(np.array((u, v)), axis=0)
u = u / norm
v = v / norm

fig, ax = plt.subplots(1, 1)


ax.quiver(x, y, u, v, units='xy', scale=0.5, color='gray')
ax.tricontour(paralelo['x'], paralelo['y'], paralelo['V'], cmap='jet')



plt.show()

