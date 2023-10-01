import sys
input = sys.stdin.readline

def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

n = int(input())
parents = [i for i in range(n + 1)]

# 입력받은 n-2개의 섬을 연결
for _ in range(n-2):
    a, b = map(int, input().split())
    union(a, b)

# 부서진 다리 찾아서 추가하기
# 0을 포함시키면 없는 0번 섬이 출력되므로 0은 제외
res = []
for i in range(1, n + 1):
    if i == parents[i]:
        res.append(i)

print(*res)