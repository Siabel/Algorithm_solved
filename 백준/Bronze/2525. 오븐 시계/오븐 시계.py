H,M = map(int,input().split())
end_time = int(input())

while M + end_time >= 60:
    M = M - 60
    H = H + 1
    if H >= 24:
        H = 0
else:
    M = M + end_time

print(H,M)