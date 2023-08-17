n = int(input())

for test_case in range(1,n + 1):
    arr = input().split()
    lst = []
    while arr:
        lst.append(arr.pop())
    print(f'Case #{test_case}:', *lst)