N,X = map(int, input().split())
A = list(map(int,input().split()))
B = []

for i in range(0,N):
    if A[i] < X:
        B.append(A[i])

print(*B)