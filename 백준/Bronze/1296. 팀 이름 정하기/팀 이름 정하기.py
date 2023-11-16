name = input()
n = int(input())

arr = []
res = 0
idx = 0

for _ in range(n):
    team_name = input()
    arr.append(team_name)

arr.sort()

for i in range(n):
    l = name.count("L") + arr[i].count("L")
    o = name.count("O") + arr[i].count("O")
    v = name.count("V") + arr[i].count("V")
    e = name.count("E") + arr[i].count("E")
    love = ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e)) % 100

    if res < love:
        res = love
        idx = i

print(arr[idx])