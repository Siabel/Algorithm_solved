t = int(input())

def lcm(a, b) :
    if b == 0:
        return a
    else :
        return lcm(b, a % b)

for _ in range(t):
    a, b = map(int, input().split())
    res = lcm(a,b)
    print(res * (a // res) * (b // res))