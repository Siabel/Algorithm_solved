a, b = input().split()
na = 0
nb = 0

for i in range(len(a)):
    na += int(a[i])
    
for j in range(len(b)):
    nb += int(b[j])

print(na * nb)