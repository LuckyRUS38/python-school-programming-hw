import numpy as np

# Загрузка данных из файла
filename = 'array.txt'
data = np.loadtxt(filename)

# Извлечение первой, двадцатой и последней колонок
first_column = data[:, 0]
twentieth_column = data[:, 19]
last_column = data[:, -1]

# Вычисление среднего арифметического и округление до целого
mean_first = int(round(np.mean(first_column)))
mean_twentieth = int(round(np.mean(twentieth_column)))
mean_last = int(round(np.mean(last_column)))

# Вывод результата
print(mean_first, mean_twentieth, mean_last)
a, b = map(int, input().split())
i = 0
result = 0

while i < abs(b):
    i += 1
    result += a
if b < 0:
    result = result * -1
    print(result)
else:
    print(result)
