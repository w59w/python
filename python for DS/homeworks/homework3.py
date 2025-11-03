# task 1
str1 = input("enter anything: ")
str2 = input("enter anything: ")
string1 = str1 + " " + str2
print(string1)

# task 2
str_ = input("enter anything: ")
print(str_*3)

# task 3
str3 = 'Data Science is about working with big data'
string3 = str3.replace('a', '#')

# task 4
name = input("enter your name: ")
surname = input("enter your surname: ")
format = f"{surname} {name} - отличный студент!"
print(format)

# task 5
code = input("enter the code og your region: ")
if code == "01":
    print("Bishkek")
elif code == "02":
    print("Osh")
elif code == "03":
    print("Batken oblast")
elif code == "04":
    print("Djalal-Abad oblast")
elif code == "05":
    print("Oshskaya oblast")
elif code == "07":
    print("Talasskaya oblast")
elif code == "08":
    print("Chuiskaya oblast")
else:
    print("invalid code")

# task 6
string6 = input("enter word")
if string6 == string6.upper():
    print("uppercase string")
elif string6 == string6.lower():
    print("lowercase string")
else:
    print("other")

# task 7
string7 = input("enter: ")
if string7 == string7.isdigit():
    print("number")
elif string7 == string7.isalpha()
    print("alpha")
else:
    print("other")

# task 8
string8 = input("enter anything: ")
if string8.startswith("Data Science"):
    print(True)
else:
    print(False)

# task 9
strin = input("enter anything: ")
string9 = strin[-1] + strin[1:-1] + strin[0]
print(string9)

# task 10
s = input("enter anything: ")
string10 = s[::-1]
print(string10)