area, num = map(int, input().split())
arr = list(map(int, input().split()))

total = area * num
result = []

for i in arr:
    result.append(i - total)
    
print(*result)