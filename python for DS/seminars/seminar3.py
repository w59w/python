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
пальто на руку. Он непременно думает, что все, кому он знаком говорят про себя: "Ах, сегодня "name" неотразим!" После 
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
