import math
import numpy as np

y = np.array([3.73, 3.53, 3.75, 3.63, 3.82])  # Readings

n = len(y)
y_snitt = sum(y) / n

s = math.sqrt(
    sum((y - y_snitt)**2) / (n - 1)
)

print(f'Gjennomsnittet er: {round(y_snitt, 2)}s')
print(f'Standardavviket er: {round(s, 2)}s')

SE = s / math.sqrt(n)

print(f'Standardfeil er {round(SE, 2)}s')
