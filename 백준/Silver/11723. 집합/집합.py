import sys
input = sys.stdin.readline

S = set()
num = [i for i in range(1, 21)]
n = int(input())

for _ in range(n):
    arr = input().split()
    if len(arr) == 1:
        if arr[0] == "all":
            S.update(num)
        elif arr[0] == "empty":
            S = set()
        continue
    
    m = int(arr[1])
    if arr[0] == "add":
        S.add(m)
    elif arr[0] == "remove":
        S.discard(m)
    elif arr[0] == "check":
        if m in S:
            print(1)
        else:
            print(0)
    elif arr[0] == "toggle":
        if m in S:
            S.remove(m)
        else:
            S.add(m)