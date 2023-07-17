A,B,C = map(int, input().split())
money = 0

if A == B == C:
    money = 10000 + A * 1000
elif A == B or B == C or A == C:
    if A == B:
        money = 1000 + A * 100
    elif A == C:
        money = 1000 + C * 100
    elif B == C:
        money = 1000 + B * 100
else:
    money = max(A, B, C) * 100

print(money)