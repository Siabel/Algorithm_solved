import sys
input = sys.stdin.readline
test_case = int(input())
res = []
for _ in range(test_case):
    a, b = map(int, input().split())
    b %= 4
    if b % 4 == 0 :
        b = 4
    if a**b % 10 == 0:
        res.append(10)
    else:
        res.append(a**b % 10)

for i in res:
    print(i)