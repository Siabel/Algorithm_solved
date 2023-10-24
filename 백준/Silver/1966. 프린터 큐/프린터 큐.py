T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    order = [x for x in range(len(lst))]

    cnt = 0

    while True:
        if lst[0] >= max(lst):
            cnt += 1
            if order[0] == m:
                break
            else:
                lst = lst[1:]
                order = order[1:]

        else:
            lst = lst[1:] + lst[:1]
            order = order[1:] + order[:1]
    print(cnt)