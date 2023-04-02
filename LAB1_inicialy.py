# Kacper Przestrzelski
# Rozwiazanie zadania przedstawia dwa sposoby rysowania liter:
# Litera K została wygenerowana ze strony victoriakrist,
# natomiast litera P została napisana przeze mnie

import matplotlib.pyplot as plt
import numpy as np
# zapis litery z generatora
def drawShapeK(ctx, xoff, yoff):
    x = np.array([105, -96, -65, -80, -95, -13, -14, -15, -23, 113, 101, 89, 167, 157, 147, -16, -28, -40, 142, 128, 114, 85, 73, 61, -31, -33, -35, -23, -42, -57, -79, -94])
    y = np.array([61, 46, 435, 434, 433, 425, 440, 455, 260, 436, 444, 452, 395, 406, 417, 182, 191, 200, 77, 82, 87, 72, 63, 54, 127, 142, 157, 60, 59, 58, 62, 61])
    plt.plot(x + xoff, y + yoff, 'k')
    plt.axis('equal')
# zapis własny litery
def drawShapeP(ctx, xoff, yoff):
    x = np.array([100, 100, 300, 330, 350, 330, 300, 150, 150, 260, 300, 270, 150, 150, 100])
    y = np.array([50, 450, 450, 400, 350, 300, 250, 250, 290, 290, 350, 400, 400, 50, 50])
    plt.plot(x + xoff, y + yoff, 'k')
    plt.axis('equal')

# rysowanie liter K i P
drawShapeK(None, 0, 0)
drawShapeP(None, 150, 0)

# wyświetlanie rysunku
plt.show()
