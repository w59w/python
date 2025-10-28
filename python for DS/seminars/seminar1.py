import math as mt

# task 1
print(2*(3-1))
print((5-1)*(5+1))
print(0.3*(4-1))
print((91-1)*(2+1))
print((5*4/3)**1/2)
print(1/3 + 5 * ((0.2 - 0.001)/91))
print((40-(4.25 * 7.08 + 6.768 / 0.75))*2050)
print((0.16 * (3.2 - 3/40) + 2*3/11 * 4.125 / 3*3/4)/(5*1/6 * 0.3 - 0.3 * 4.5 + 1/3 * 0.3))

# task 2
x = 24
y = 31.4
print(type(x))
print(type(y))

# task 3
a = 5
b = 3
diff = abs(a - b)
print(diff)

# task 4
vsego_kg = 290
odin_meshok = 25
print(vsego_kg / odin_meshok)
print(vsego_kg % odin_meshok)

# task 5
h_1 = 13
m_1 = 25
h_2 = 19
m_2 = 40
h = h_1 - h_2
m = m_1 - m_2
print(h, m)

# task 6
old_price = int(input("write old price: "))
new_price = int(input("write new price: "))
res = round((old_price - new_price)/100, 1)
print(res)

# task 7
x = 2
y = mt.exp(1/(1 + mt.cos(x)**2))
print(y)

# task 8
zakaz = 1500
odin_operator = 45
res2 = zakaz / odin_operator
print(f"Для выполнения заказа необходимо задействовать {res} поста.")

# task 9
katet1 = int(input("введите длину катета 1: "))
katet2 = int(input("введите длину катета 2: "))
gip = int(input("введите длину гипотенузы: "))
min_katet = min(katet1, katet2)
sin_menshego = min_katet / gip
print(sin_menshego)

# task 10
ugol_v_radianah = mt.asin(sin_menshego)
gradusy_ugla = ugol_v_radianah * 180 / mt.pi
print(gradusy_ugla)
