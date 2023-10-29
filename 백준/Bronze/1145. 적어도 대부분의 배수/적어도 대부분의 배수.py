arr = list(map(int, input().split()))

min_n = min(arr)
cnt = 0

while True:
    cnt = 0
    for i in range(len(arr)):
        if min_n % arr[i] == 0 :
            cnt += 1
    if cnt >= 3:
        print(min_n)
        break
    min_n += 1