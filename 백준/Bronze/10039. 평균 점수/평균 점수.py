res = 0

for i in range(5):
    score = int(input())
    if score < 40:
        score = 40
    res += score
print(res // 5)