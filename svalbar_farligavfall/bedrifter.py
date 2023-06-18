import numpy as np
import matplotlib.pyplot as plt

neringsliv = np.loadtxt("data/data2.csv", delimiter=";", skiprows=2)


plt.plot(neringsliv[0], neringsliv[1])

plt.show()
