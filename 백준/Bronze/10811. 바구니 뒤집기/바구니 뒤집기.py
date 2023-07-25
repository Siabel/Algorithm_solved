N,M = map(int,input().split())
result = []

for a in range(N) :
    result.append(a+1)

for b in range(M) :
    i, j = map(int, input().split())
    midValue = result[i-1:j:]
    midValue.reverse()
    result = result[:i-1:] + midValue + result[j::]
    
print(*result)