print("skriv inn koords til vektorene u = [x1, y1]")

x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

print("skriv inn korrd til vektorene v = [x2, y2]")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

skalargreie = x1*x2 + y1*y2

if skalargreie == 0:
    print("vektorene er ortogonale")
    
elif skalargreie > 0:
    print("vektorene er spiss")
else:
    print("vektorene er stumme")
print(skalargreie)