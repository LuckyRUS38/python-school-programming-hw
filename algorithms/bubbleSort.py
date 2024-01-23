# --------------------------------#
#  Алгоритм сортировки пузырьком  #
# --------------------------------#
import random

a = []
for i in range(1000):
    a.append(random.randint(-100000, 100000))
N = len(a)

for i in range(0, N-1):
    for j in range(0, N-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)
