N = int(input())
num = int(input())

cnt = 0
for i in range(N):
    cnt += num % 10
    num = num//10
    
print(cnt)