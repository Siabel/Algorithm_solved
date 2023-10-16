n = int(input())
res = 0

min_num = n - (9 * len(str(n)))
if min_num < 0:
    min_num = 0

for i in range(min_num, n):
    if n == i + sum(int(j) for j in str(i)):
        if i > res:
            res = i
            break

print(res)