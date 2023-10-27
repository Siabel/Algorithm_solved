n = input()
f = int(input())
min_n = n[:-2] + '00'
min_n = int(min_n)

res = f

while True:
    if min_n % f == 0:
        break
    else:
        min_n += 1

print(str(min_n)[-2:])