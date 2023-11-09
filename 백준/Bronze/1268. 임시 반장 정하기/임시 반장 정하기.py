n = int(input())
students = [list(map(int, input().split())) for _ in range(n)]

max_friend = -1
res = -1

for i in range(n):
    check = set()
    for j in range(5):
        for k in range(n):
            if students[i][j] == students[k][j]:
                check.add(k)
    
    if len(check) > max_friend:
        res = i + 1
        max_friend = len(check)
    
print(res)