T = int(input())

for test_case in range(1, T + 1):
    res = 0
    num_lst = list(map(int, input().split()))
    for i in num_lst:
        if i % 2 != 0:
            res += i
    print(f'#{test_case} {res}')