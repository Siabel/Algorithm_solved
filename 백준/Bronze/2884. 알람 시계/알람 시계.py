H,M = map(int,input().split())

if M-45 < 0:
    M = M-45+60
    H = H-1
    if H < 0:
        H = 23 
else: 
    M = M-45

print(H, M)