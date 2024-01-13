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
