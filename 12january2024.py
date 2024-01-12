# 8
age = int(input("Введите ваш возраст (целое число, не превышающее 120): "))
if 10 <= age % 100 <= 20:
    print(age, "лет")
elif age % 10 == 1:
    print(age, "год")
elif 2 <= age % 10 <= 4:
    print(age, "года")
else:
    print(age, "лет")

# 9A
x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
print(x <= 1 and y <= 1)

# 9C
x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
print(x**2 + y**2 <= 1)
