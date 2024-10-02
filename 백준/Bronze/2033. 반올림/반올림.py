n = int(input())

x = 10
while n > x:
    temp = n % x
    
    if temp >= x // 2:
        n += x
        
    n -= temp
    x *= 10

print(n)