# 에라토스테네스의 체
def is_prime_num(a):
    arr = [1] * (a + 1)
    arr[0] = 0
    arr[1] = 0

    for i in range(2, a + 1):
        if arr[i] == 1:
            j = 2

            while (i * j) <= a:
                arr[i * j] = 0
                j += 1

    return arr

n, m = map(int, input().split())
arr = is_prime_num(m)

for i in range(n, m + 1):
    if arr[i] == 1:
        print(i)