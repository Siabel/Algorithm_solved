a = int(input())
b = int(input())
c = int(input())

num = str(a * b * c)
lst = [0 for _ in range(10)]

for i in num:
    lst[int(i)] += 1

for i in range(10):
    print(lst[i])
