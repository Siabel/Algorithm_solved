num = []

for i in range(0,9):
    N = int(input())
    num.append(N)

A = int(max(num))
print(A)
print(num.index(A)+1)