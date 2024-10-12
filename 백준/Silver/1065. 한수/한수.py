n = int(input())
cnt = 0

for i in range(1, n + 1):
    if i < 100:
        cnt += 1
    else:
        a = i // 100
        b = (i // 10) % 10
        c = i % 10

        if a - b == b - c:
            cnt += 1

print(cnt)