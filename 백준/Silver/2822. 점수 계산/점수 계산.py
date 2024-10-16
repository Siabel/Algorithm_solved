score = []

for _ in range(8):
    score.append(int(input()))
    
arr = []
res = 0
for i in range(5):
    res += max(score)
    arr.append(score.index(max(score)) + 1)
    score[score.index(max(score))] = -1
    
arr.sort()
print(res)
print(*arr)