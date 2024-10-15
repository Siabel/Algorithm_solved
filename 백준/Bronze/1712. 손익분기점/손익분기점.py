a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    res = a // (c - b)
    print(res + 1)