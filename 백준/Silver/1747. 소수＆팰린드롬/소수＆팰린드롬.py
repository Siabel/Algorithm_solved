# 에라토스테네스의 체
def is_prime_num(a):
    arr = [1] * (a + 1)
    arr[0] = 0
    arr[1] = 0

    for i in range(2, int(a ** 0.5) + 1):
        if arr[i] == 1:
            for j in range(i+i, a, i):
                if arr[j] == 1:
                    arr[j] = 0

    return arr

# 팰린드롬
def is_palindrome(word):
    word = str(word)
    tmp = word[::-1]
    if word == tmp:
        return True
    else:
        return False

n = int(input())
arr = is_prime_num(int(1e7))

res = 0

for i in range(n, len(arr)):
    if arr[i] and is_palindrome(i):
        res = i
        break

print(res)