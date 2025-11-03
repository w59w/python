# task 1
# a = 32
# b = 3.5
# x = True

a = "32"
b = "3.5"
x = "True"

print(type(a))
print(type(b))
print(type(x))

# task 2
str_ = input("enter 'hello my friend!': ")
print(str_)

# task 3
name = input("Write your name: ")
surname = input("Write your surname: ")
print(name, surname)

# task 4
res = name + " " + surname

# task 5
name = input("Write your name: ")
score = input("Write your score: ")
print("Hello, " + name + ", your score is " + score)

# task 6
name = input("Write your name: ")
age = input("Write your age: ")
print(f"menya zovut {name}, i mne {age} let")

# task 7
stroka = "python is easy"
print(stroka[0])  # pervyi simvol
print(stroka[-1])  # poslednyi simvol
print(stroka[:2])  # dva pervyh simvola
print(stroka[-3:])  # tri poslednih
print(stroka[2:5])
print(stroka[1:9])
print(stroka[1:])
print(stroka[0::1])
print(stroka[1::1])
print(stroka[::-1])
print(stroka[4:1:-1])
print(stroka[::-2])

# task 8

stroka2 = "PythonProgrammingLnguage"
word1 = stroka2[:6]
word2 = stroka2[-8:]
result = word1 + " " + word2
print(result)

# task 9
stroka3 = "I love Python Programming!"
srez = stroka3.replace("Python", "Java")
print(srez)

# task 10
name = input("Write your name: ")
name = name.capitalize()
print("Hi,", name, "!")

# task 11
code = 'atgcaagttgacaattta'
code = code.upper()
print(code)

# task 12
code1 = code = 'augcaagugacaauuua'
code1 = code1.replace("u", "t")
print(code1)

# task 13
nun_phone = '   +7(919)-@784-54_18@@     '
nun_phone = nun_phone.strip()
for sym in [" ", "_", "@"]:
    nun_phone = nun_phone.replace(sym, "")
print(nun_phone)

# task 14
str4 = '67dg#uin_87'
print(len(str4))
print(str4.index("#"))

# Task 15
# name = input("Write the name: ")
# text = """ Имя этого героя "name". Поход в театр для него целый ритуал. Входя в фойе, "name" демонстративно снимает
# шляпу, поправляет галстук и вешает
# пальто на руку. Он непременно думает, что все, кому он знаком говорят про себя: "Ах, сегодня "name" неотразим!" После
# чего "name"
# занимает лучшее место бенуара и с важным видом достает очки."""
# print(f"Имя этого героя {name}. Поход в театр для него целый ритуал. Входя в фойе, {name} демонстративно снимает
# шляпу, поправляет галстук и вешает "
#       f" пальто на руку. Он непременно думает, что все, кому он знаком говорят про себя: 'Ах, сегодня {name}
#       неотразим!' После чего {name}"
#       f"занимает лучшее место бенуара и с важным видом достает очки")

name = input("Write your name: ")
name1 = name.capitalize()
text = """ Имя этого героя "name". Поход в театр для него целый ритуал. Входя в фойе, "name" демонстративно снимает 
шляпу, поправляет галстук и вешает
пальто на руку. Он неплвременно думает, что все, кому он знаком говорят про себя: "Ах, сегодня "name" неотразим!" После 
чего "name"
занимает лучшее место бенуара и с важным видом достает очки."""
text1 = text.replace('"name"', name1)
print(text1)

# task 16
str1 = '84hj#55hjl'
# index = str1.index('#')
# result = str1[index+1:] + 'abc' + str1[:index:]
# print(result)

str2 = str1[0:5]
str3 = str1[5:]
str4 = "abc"
print(str2 + str4 + str3)

# task 17
tel = '0777784500'
formatted = f'+996 ({tel[1:4]}) {tel[4:7]}-{tel[7:]}'
print(formatted)

# task 18
stroka_3 = input("vvedite text: ")
if len(stroka_3) > 5:
    print("too long")
else:
    print(stroka_3)

# task 19
# stroka3 = input("vvedite text: ")
# if len(stroka3) > 5:
#     print("too long")
#     print("vvedite text eshe raz")
#     if stroka3 == stroka3:
#         print(stroka3)
# else:
#     print("incorrect")

str1 = input("vvedite parol: ")
if len(str1) > 5:
    str2 = input("vvedite parol eshe raz: ")
    if str1 == str2:
        print(str2)
    else:
        print("not match")
else:
    print("incorrect")

# task 20

parol = input("vvedite parol: ")
if "@" in parol or "#" in parol or "%" in parol:
    if len(parol) >= 8:
        parol2 = input("vvedite parol eshe raz: ")
        if parol2 == parol:
            print("parol is correct")
        else:
            print("not match")
    else:
        print("corotco")
else:
    print("incorrect")

# task 21

parol1 = input("vvedite parol: ")
if "@" in parol1 or "#" in parol1 or "%" in parol1:
    if len(parol) >= 8:
        parol3 = input("vvedite parol eshe raz: ")
        if parol3 == parol1:
            print("parol is correct")
        else:
            print("not match")
    else:
        print("corotco")
else:
    print("invalid password. please re-enter!")
    parol4 = input("vvedite parol eshe raz: ")
    if "@" in parol4 or "#" in parol4 or "%" in parol4:
        if len(parol) >= 8:
            parol5 = input("vvedite parol eshe raz: ")
            if parol5 == parol4:
                print("passwor '***' is saved!")
            else:
                print("not match")
        else:
            print("corotco")
    else:
        print("You have exhausted the number of attempts!")

    # task 22
    name_list = ["Kumushai", "Aidana", "Amina", "Sabina"]
    name5 = input("Enter your anme: ")
    if name5 in name_list:
        print("Pozdravlyayu, u vas povyshennaya stipendiya.")
    else:
        print("Uvy, Vashego imeni v spiske net.")

    # task 23
    code5 = 'GGGGGGGGGAATTATGATCCTTACTTT'
    if code5.startswith("G"):
        code5 = "A" + code5[1:]

    count_g = code5.count("G")

    if count_g < 5:
        code5 = code5 + "GGG"

    print(code5)

# task 24
names = input("Enter your names: ")
nam1, nam2 = names.split()
print(nam1, '\n', nam2)

# task 25
prod_name = input("Enter your product name: ")
old_price = int(input("Enter the old price: "))
new_price = int(input("Enter the new price: "))
podorojala = (new_price - old_price) / 100
print(f"the {prod_name} podorojala na {podorojala}%")

# task 26
slovo = input("vvedite slovo: ")
peremena = slovo[0] + slovo[1:-1][::-1] + slovo[-1]
print(peremena)

# task 27
aslovo = '      съешь ещё этих мягких французских булок, да выпей чаю      '
count_s = aslovo.count(" ") + 1
print(count_s)

# task 28
slovov = 'sksjhkjn23456kjhkjhkxcv1234'
slovov1 = len(slovov) // 2
if len(slovov) % 2 != 0:
    slovov1 = slovov1 + 1

part1 = slovov[:slovov1]
part2 = slovov[slovov1:]

new_slovov = part1 + part2
print(new_slovov)

# task 29
dvaslova = "razdelyaem stroku"
wo = dvaslova.split()
new_sl = wo[1] + " " + wo[0]
print(new_sl)

# task 30
fs = 'sksjhkjn23456kjhkjffhkxcv12ffff34'
f_count = fs.count("f")

if f_count == 1:
    print(fs.find("f"))
elif f_count >= 2:
    print(fs.find("f"), fs.rfind("f"))

# task 31
hs = '09drh121985fh0u91'
hs1 = hs.find("h")
hs2 = hs.find("h")
resu = hs[:hs1] + hs[hs1 + 1]
print(resu)

# task 32
s = "Engagementeng"
if s[:3].lower() == s[-3:].lower():
    resul = s[::-1]
else:
    resul = s

print(resul)

# task 33
lp = ["cigarets", "pivo", "vino", "konyak", "vodka"]
nt = input("vvedite nazvanie tovara: ").lower()
if any(item in lp for item in nt):
    age = int(input("vvedite vash vozrast: "))
    if age >= 18:
        print("uspeshnaya pokupka!")

# task 34
name1 = input("vvedite imya pervogo studenta: ")
math1 = int(input(f"{name1} - Math: "))
eng1 = int(input(f"{name1} - Eng: "))

name2 = input("vvedite imya vtorogo studenta: ")
math2 = int(input(f"{name2} - Math: "))
eng2 = int(input(f"{name2} - Eng: "))

avg1 = (math1 + eng1) / 2
avg2 = (math2 + eng2) / 2

print("\nNmae\tMath\tEnglish\tAverage")
print(f"{name1}\t{math1}\t{eng1}\t{avg1:.1f}")
print(f"{name2}\t{math2}\t{eng2}\t{avg2:.1f}")

# task 35
brands = ["Acer", "Asus", "Honor", "HP", "Lenovo"]
prices = [20000, 35000, 50000, 40000, 25000]

brand_input = input("vvedite imya brenda: ")
if brand_input in brands:
    i = brands.index(brand_input)
    base = prices[i]
    i5 = base * 1.2
    i7 = base * 1.45

    print(f"{brand_input}: ")
    print(f"i3: {base:.0f} som")
    print(f"i5: {i5:.0f} som")
    print(f"i7: {i7:.0f} som")
else:
    print("takogo brenda net v spiske.")

# task 36
A = input("Ввудите координаты точки А (ха уа) через пробел: ").strip()
B = input("Введите координаты точки B (xb yb) через пробел: ").strip()
xa, ya = map(float, A.split())
xb, yb = map(float, B.split())
k = (yb - ya) / (xb - xa)
b = ya - xa * k
print(f"k = {k:.2f}")
print(f"b = {b:.2f}")
