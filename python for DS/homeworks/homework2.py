# task 1
number = int(input("enter a number: "))
if number > 0:
    print(True)
else:
    print(False)

# task 2
mark = int(input("enter a mark: "))
if mark >= 90:
    print("Отлично, Ваша оценка 5!")
elif 90 > mark >= 80:
    print("Здорово, Ваша оценка 4!")
elif 80 > mark >= 70:
    print("Хорошо, Ваша оценка 3!")
elif 70 > mark >= 60:
    print("Вам стоит подучить материал.")
else:
    print("Вы не сдали экзамен.")

# task 3
x = int(input("enter a number: "))
y = int(input("enter a number: "))
z = int(input("enter a number: "))
if x < y and x < z:
    print(x)
elif y < x and y < z:
    print(y)
else:
    print(z)

# task 4
x1 = int(input("enter a number: "))
y1 = int(input("enter a number: "))
if x1 % y1 == 0:
    print(x1 / y1)
else:
    print(x1 + y1)

# task 5
a = int(input("vvedite storony treugolnika: "))
b = int(input("vvedite storonu treugolnika: "))
c = int(input("vvedite storonu treugolnika: "))
if a + b > c:
    print("yes")
elif b + c > a:
    print("yes")
elif c + a > b:
    print("yes")
else:
    print("no")

# task 6
a1 = int(input("vvedite chislo: "))
b1 = int(input("vvedite chislo: "))
c1 = int(input("vvedite chislo: "))
if a1 + b1 == c1:
    print(True)
else:
    print(False)

# task 7
chislo = int(input("vvedite chislo: "))
if 10 < chislo >= 2:
    print(True)
else:
    print(False)

# task 8
chislo1 = int(input("vvedite chislo: "))
if 5 >= chislo1 < 4:
    print(True)
else:
    print(False)

# task 9
x2 = int(input("vvedite chislo: "))
if x2 in {2, 4, 6, 8, 10}:
    print(True)
else:
    print(False)

# task 10
x4 = int(input("vvedite chislo: "))
if -10 < x4 < 5 or 5 < x4 <= 7 or 8 < x4:
    print(True)
else:
    print(False)

# task 11
x5 = int(input("vvedite chislo: "))
if ((x5**2 - 3*x5) / (x5 + 5)) >= ((x5-3)/(7-x)):
    print(True)
else:
    print(False)

# task 12
x6 =int(input("vvedite chislo: "))
if (x6**2 - 3*x6) <= 0 and (x6**2 - 6*x6 +8) > 0:
    print(True)
else:
    print(False)

# task 13
x7 = int(input("vvedite chislo: "))
if (x7 - 3 > 5) or (x7 <= 2):
    print(True)
else:
    print(False)
