# Ввод значений A, B, C
A = int(input())  # общая сумма денег у Фёдора
B = int(input())  # стоимость бутылки с соком
C = int(input())  # стоимость пустой бутылки

# Начальное количество бутылок, которое может купить Фёдор
bottles = A // B

# Оставшиеся деньги после первоначальной покупки
remaining_money = A % B

# Покупка дополнительных бутылок, сдавая пустые
while remaining_money + C >= B:
    bottles += 1
    remaining_money = remaining_money + C - B

# Вывод количества бутылок
print(bottles)
