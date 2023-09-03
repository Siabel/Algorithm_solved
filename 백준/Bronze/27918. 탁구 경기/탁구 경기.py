n = int(input())
d = 0
p = 0
for _ in range(n):
    s = input()
    if s == 'D':
        d += 1
    else:
        p += 1

    # 게임 종료
    if abs(d - p) > 1:
        print(f"{d}:{p}")
        break
else:
    print(f"{d}:{p}")
   