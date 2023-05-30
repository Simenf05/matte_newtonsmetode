import math
import numpy as np
import matplotlib.pyplot as plt

lengde = np.array([20, 40, 60, 80, 100])
y_snitt = np.array([1.33, 2.06, 2.74, 3.26, 3.69])
SE = np.array([0.06, 0.07, 0.08, 0.04, 0.05])

plt.plot(lengde, y_snitt, "b.")

plt.vlines(lengde, y_snitt - 2*SE, y_snitt + 2*SE, "r")

plt.xlabel("Lengde (cm)")

plt.ylabel("Tid (sekunder)")

x = np.linspace(10, 110, 100)
y = 0.195 * x ** 0.6413

plt.plot(x, y, "--")

plt.show()
