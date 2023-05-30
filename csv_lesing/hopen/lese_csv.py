import numpy as np
import matplotlib.pyplot as plt

hopen = np.loadtxt("table.csv", delimiter=";", skiprows=1, usecols=(2, 3))

aar = hopen[:, 0]
temp = hopen[:, 1]

plt.plot(aar, temp)

plt.xlabel("År")
plt.ylabel("Temperatur (i grader C)")

k = 7

temp_glatt = []

for i in range(k, len(temp) - k):
    temp_glatt.append(np.mean(temp[(i - k):(i + k)]))

plt.plot(aar[k:len(temp) - k], temp_glatt, "k")

plt.show()
