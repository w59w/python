import math
# task 1
x = int(input("Vvedite chislo: "))
if x > 5:
    print(True)
else:
    print(False)

# task 2
y = int(input("Vvedite chislo:"))
if y % 2 == 0:
    print(True)
else:
    print(False)

# task 3
a = int(input("Vvedite chislo: "))
b = int(input("Vvedite chislo:"))
if a / b == 2:
    print(True)
else:
    print(False)

# task 4
c = int(input("Vvedite chislo:"))
if c % 3 == 0:
    print("Yes")
else:
    print("No")

# task 5
d = int(input("Vvedite chislo: "))
if not d % 2 == 0:
    d += 1
    print(d)
else:
    print(d)

# task 6
e = int(input("Vvedite chislo:"))
if (e > 3) and (e <= 8):
    print("Yes")
else:
    print("No")

# task 7
f = int(input("Vvedite chislo: "))
if (f >= 5) and (f < 15) and (f != 10):
    print("Yes")
else:
    print("No")

# task 8
g = int(input("Vvedite chislo:"))
if (g <= 5) and (g > 10):
    print("Yes")
else:
    print("No")

# task 9
h = int(input("Vvedite chislo: "))
if (h > 2) and (h <= 6) or (h > 10):
    print("yes")
else:
    print("no")

# task 10
g = int(input("Vvedite chislo: "))
if (g < 4 or g > 10) and (x <= 2 or x >= 6):
    print("Yes")
else:
    print("no")

# task 11
k = int(input("Vvedite chislo:"))
if (k > 5) or (k <= 3):
    print("yes")
else:
    print("no")

# task 12
l1 = int(input("Vvedite chislo:"))
if (l1 > 5) or (l1 <= 3):
    print("yes")
elif 3 < l1 <= 6:
    print("yes")
elif l1 >= 4:
    print("yes")
elif (-2 < l1 <= 3) or (l1 > 5):
    print("yes")
elif (0 < l1 < 4) or (6 <= l1 < 10):
    print("yes")
else:
    print("no")

# task 13
ugol = int(input("Vvedite chislo: "))
if 40 <= ugol <= 45:
    print("parametry optimalny")
elif 40 < ugol:
    print("korabl razrushitsya v atmosphere")
else:
    print("controlliruemyi spusk nevozmojen")

# task 14
x1 = int(input("Vvedite chislo x: "))
y1 = int(input("Vvedite chislo y: "))
line = 0.5 * x + 4
if y > line:
    print("higher")
elif y < line:
    print("below")
else:
    print("on line")

# task 15

# task 16
num1 = int(input("Vvedite chislo: "))
num2 = num1 ** 1 / 2
if num1 / num2 == 3:
    print("ok")
else:
    print("not ok")

# task 17
num4 = int(input("Vvedite chislo: "))
num5 = int(input("Vvedite chislo: "))
if (num4 + num5) > 0 < (num4 - num5):
    print("++")
elif (num4 + num5) > 0 > (num4 - num5):
    print("+-")
elif (num4 + num5) < 0 < (num4 - num5):
    print("-+")
elif (num4 + num5) < 0 > (num4 - num5):
    print("--")
else:
    print("vvedite chisla!")

# task 18


a = int(input("Vvedite chislo: "))
b = int(input("Vvedite chislo: "))
c = int(input("Vvedite chislo: "))
D = b ** 2 - 4 * a * c
if D < 0:
    print("kornei net")
elif D == 0:
    x = -b / (2 * a)
else:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)

# task 19
aa = int(input("Vvedite chislo: "))
bb = int(input("Vvedite chislo: "))
cc = int(input("Vvedite chislo: "))
if (aa + bb > cc) or (aa + cc > b) or (bb + cc > a):
    print("eto treugolnik")
else:
    print("eto ne treugolnik")

# task 20
aaa = int(input("Vvedite chislo: "))
bbb = int(input("Vvedite chislo: "))
ccc = int(input("Vvedite chislo: "))
max_side = max([aaa, bbb, ccc])
if max_side == aaa:
    cat1, cat2 = bbb, ccc
elif max_side == bbb:
    cat1, cat2 = aaa, ccc
else:
    cat1, cat2 = aaa, bbb

if max_side ** 2 == cat1 ** 2 + cat2 ** 2:
    print("eto pryamougolni treugolnik")
else:
    print("eto ne pryamougolni treugolnik")
