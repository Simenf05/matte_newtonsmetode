import numpy as np
import matplotlib.pyplot as plt


farlig_avfall = np.loadtxt("data/excel_export.csv", delimiter=",", skiprows=2)

aar = farlig_avfall[:, 0]

avfall = farlig_avfall[:, 1:]

small_data = []
big_data = []

for x in range(len(avfall[0])):
    current_avfall = avfall[:, x - 1]
    if current_avfall[0] > 100:
        big_data.append(current_avfall)
    else:
        small_data.append(current_avfall)


fig, ax1 = plt.subplots()

ax1.set_xlabel('år')
ax1.set_ylabel('big --')
for x in big_data:
    ax1.plot(aar, x, '--')

ax2 = ax1.twinx()

ax2.set_ylabel('small -')
for x in small_data:
    ax2.plot(aar, x, '-')

fig.tight_layout()
plt.show()
