# # 12.01
# # 1
# a = int(input())
# b = int(input())
#
# for i in range(a, b+1):
#     print(f'{i}*{i}={i*i}')
# # 2
# a = int(input())
# b = int(input())
# i = 0
# result = 0
#
# while i < abs(b):
#     i += 1
#     result += a
# if b < 0 or a < 0:
#     result = result * -1
#     print(result)
# 3
x = int(input())
a, b = 1, 1

for i in range(1, x + 1):
    print(i, '=>', a)
    a, b = b, a + b
