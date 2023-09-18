def getMyDivisor(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList

a,b = map(int, input().split())

arr_a = getMyDivisor(a)
arr_b = getMyDivisor(b)
res = []

for i in arr_a:
    for j in arr_b:
        if i == j:
            res.append(i)

com_div = max(res)
com_mul = a * b // com_div

print(com_div)
print(com_mul)