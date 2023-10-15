n, k = map(int, input().split())

n1 = 1
for num in range(n, n - k, -1):
    n1 *= num

n2 = 1
for num in range(1, k + 1):
    n2 *= num

print(n1 // n2)