x = int(input())
i, num = 0, 0

while x > num:
    i += 1
    num += i

if i % 2 == 0:
    a = i - (num - x)
    b = (num - x) + 1
else:
    a = (num - x) + 1
    b = i - (num - x)

print(f'{a}/{b}')