N, m, M, T, R = map(int, input().split())

min_minute = m
minute = 0
res = 0
if m > M or m + T > M:
    res = -1
else:
    while True:
        m += T
        if m <= M:
            minute += 1
            res += 1
        else:
            m -= T
            m -= R
            if m < min_minute:
                m = min_minute
            res += 1
        if minute >= N:
            break
print(res)