def self_number(n):
    num = n
    while n != 0:
        num += n % 10
        n //= 10
    return num
        
result = []

for i in list(range(1, 10001)):
    result.append(self_number(i))
    if i not in result:
        print(i)