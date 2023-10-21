L = int(input())
arr = input()
res = 0

for i in range(L):
    res += (ord(arr[i])-96) * (31 ** i)
    
print(res % 1234567891)