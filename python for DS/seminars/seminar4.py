# task 1

list1 = []
list2 = list()
print(f"Type of list1: {type(list1)}")
print(f"Type of list2: {type(list2)}")

# task 2
list3 = [1, 2, 3]
print(list3)

# task 3
list4 = list(range(1, 20))
print(list4)

# task 4
list5 = list(range(0, 20, 2))
print(list5)

# task 5
list6 = list(range(1, 13, -1))
print(list6)

# task 6
str_ = "abcd1234"
list7 = str_.split(",")
print(list7)

# task 7
brands = 'Acer, HP, Lenovo, Asus, Honor, Apple, Toshiba, Samsung'
list8 = brands.split(",")
print(list8)

# task 8
num_str = input("Enter numbers: ")
num_list = num_str.split(",")
print(num_list)

# task 9
tovary = input("enter nazvaniya tovarov cherez _: ")
if "_" in tovary:
    list9 = tovary.split(",")
    print(list9)
else:
    print("nothing")

# task 10
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(list_[0])
print(list_[-2])
print(list_[3:-2:])
print(list_[3::1])
print(list_[::-1])
print(list_[-2:0:1])

# task 11

