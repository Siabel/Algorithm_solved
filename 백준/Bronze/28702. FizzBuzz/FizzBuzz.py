import sys
input = sys.stdin.readline

arr = [input().strip() for _ in range(3)]

# 역순으로 숫자인거 찾기
for i in range(2, -1, -1):
    if arr[i].isdigit():
        ans = int(arr[i]) + (3-i)
        break

if ans % 15 == 0:
    print('FizzBuzz')
elif ans % 3 == 0:
    print('Fizz')
elif ans % 5 == 0:
    print('Buzz')
else:
    print(ans)