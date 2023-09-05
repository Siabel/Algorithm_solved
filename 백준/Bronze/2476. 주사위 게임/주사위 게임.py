n = int(input())
price_lst = []

for _ in range(n):
    a,b,c = map(int, input().split())
    if a == b == c:
        s = 10000 + a * 1000
    elif a != b and a != c and b != c:
        s = max(a,b,c) * 100
    else:
        if a == b or a == c:
            s = 1000 + a * 100
        else:
            s = 1000 + b * 100
    price_lst.append(s)

print(max(price_lst))