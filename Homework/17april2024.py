# 1
val = 4 * (625 ** 1920) + 4 * (125 ** 1930) - 4 * (25 ** 1940) - 3 * (5 ** 1950) - 1960

base_5_repr = ''
remainder = abs(val)

while remainder > 0:
    digit = remainder % 5
    base_5_repr = str(digit) + base_5_repr
    remainder //= 5
zeros_count = len(base_5_repr) - len(base_5_repr.rstrip('0'))

print(zeros_count)

# 3
max_value = -1
max_xy_decimal = -1
for x in range(39):
    for y in range(39):
        num = 12 * (39**6) + x * (39**5) + 4 * (39**4) + 5 * (39**3) + 6 * (39**2) + y * 39 + 8
        if num % 38 == 0:
            xy_decimal = x * 39 + y
            if xy_decimal > max_value:
                max_value = xy_decimal
                max_xy_decimal = xy_decimal

print(max_xy_decimal)
