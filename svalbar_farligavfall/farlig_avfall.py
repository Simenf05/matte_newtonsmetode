import numpy as np
import matplotlib.pyplot as plt

farlig_avfall = np.loadtxt("data/excel_export_2.csv", delimiter=",", skiprows=1)

aar = farlig_avfall[:, 0]

avfall = farlig_avfall[:, 1:]

for x in range(len(avfall[0])):
    current_avfall = avfall[:, x - 1]
    plt.plot(aar, current_avfall)

plt.show()
