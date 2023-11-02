n = int(input())

stack = []
res = []
flag = 0
idx = 1
for _ in range(n):
    num = int(input())
    while idx <= num:
        stack.append(idx)
        res.append("+")
        idx += 1

    if stack[-1] == num:
        stack.pop()
        res.append("-")
    else:   
        print("NO")
        flag = 1
        break               

if flag == 0:
    for i in res:
        print(i)