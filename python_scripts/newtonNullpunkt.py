import numpy as np
import matplotlib.pyplot as plt


def f(x: float):
    return x * np.log(x) - 1

x = np.linspace(0, 100, 10000)[1:]
y = f(x)

plt.plot(x, y, color = "b")
plt.ylim(-20, 40)
plt.axhline(y = 0, color = "k")
plt.axvline(x = 0, color = "k")
plt.xlabel("hgljyrfyu")
plt.ylabel("y")
plt.grid()
plt.show()

x1 = float(input("skriv inn en x verdi nærme nullpunktet: "))
delta_x = .00001
def f_derivert(a):
    return (f(a + delta_x) - f(a)) / delta_x

def ny_x_verdi(x1):
    return x1 - (f(x1) / f_derivert(x1))

for i in range(10):
    x2 = ny_x_verdi(x1)
    print(f"et bedre forslag er gitt ved x = {round(x2, 4)}.")
    x1 = x2
    
print(f"med x = {x1} er f(x) = {f(x1)}")