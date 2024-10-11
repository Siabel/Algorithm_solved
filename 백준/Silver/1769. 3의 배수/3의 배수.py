x = input()
cnt = 0

def judge_3(num_x):
    global cnt
    cnt += 1

    if len(num_x) == 1:
        if int(num_x) % 3 == 0:
            return "YES"
        else:
            return "NO"

    y = sum(int(i) for i in num_x)
    
    return judge_3(str(y))

if len(x) == 1:
    if int(x) % 3 == 0:
        print(cnt)
        print("YES")
    else:
        print(cnt)
        print("NO")
else:
    res = judge_3(x)
    print(cnt - 1)
    print(res)
