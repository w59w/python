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
list11 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list11[1] = 100
print(list11)

# task 12
list12 = [1, 2, 3, 4, 5]
list12[-2:] = [12, 13]
print(list12)

# task 13
list13 = [1, 3, 5, 4, 7, 9, 8, 10, 1, 14, 19, 20]
print(max(list13))
print(min(list13))
print(sum(list13))
print(len(list13))
print(sum(list13)/len(list13))

# task 14
brand = ['Acer', 'HP', 'Lenovo', 'Asus', 'Honor', 'Apple', 'Toshiba', 'Samsung']
index_br = brand.index("Honor")
print(index_br)

# task 15
brand = ['Acer', 'HP', 'Lenovo', 'Asus', 'Honor', 'Apple', 'Toshiba', 'Samsung']
if 'Apple' in brand:
    index = brand.index("Apple")
    brand[index] = "Irbis"
else:
    print("Apple is not found")
print(brand)

# task 16
brand = ['Acer', 'HP', 'Lenovo', 'Asus', 'Honor', 'Apple', 'Toshiba', 'Samsung']
price = [20000, 27000, 95000, 15000, 50000, 100000, 85000, 80000]
max_index = price.index(max(price))
print("Бренд с максимальной стоимостью: ", brand[max_index])

# task 17
product_name = []
price = []

user_input = input("vvedite tovar i cenu cherez '-': ")
name, cost = user_input.split('-')

name = name.strip()
cost = cost.strip()

product_name.append(name)
price.append(int(cost))

print(f"nazvaniya: {product_name}")
print(f"price: {price}")

# task 18
input_gr = input('vvedite nachalo i konec: ')
input_gr = input_gr.split()
list18 = list(range(int(input_gr[0]), int(input_gr[1])))
print(list18)

# task 19
daily_list = [1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1]
