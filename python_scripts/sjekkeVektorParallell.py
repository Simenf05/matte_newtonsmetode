import math

print("skriv inn koords for vektoren u = [x1, x2]")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

print("skriv inn koords for vektoren v = [x2, y2]")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

prikk = x1*x2 + y1*y2
lengdeu = math.sqrt(x1**2 + y1**2)
lengdev = math.sqrt(x2**2 + y2**2)

a = math.acos(prikk / (lengdeu * lengdev))
vinkel = round(math.degrees(a), 2)

if vinkel == 0 or vinkel == 180:
    print("parallelle")
elif vinkel == 90:
    print("ortogonale")
else: 
    print("ingen av delene") 
