n = int(input())
sum = 0

arr = [1, 1]
for i in range(2, 21):
    arr.append(arr[i - 1] * i)

for i in range(20, -1, -1):
    if sum + arr[i] < n:
        sum += arr[i]
    elif sum + arr[i] == n:
        print("YES")
        exit(0)

print("NO")