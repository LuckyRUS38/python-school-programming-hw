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
