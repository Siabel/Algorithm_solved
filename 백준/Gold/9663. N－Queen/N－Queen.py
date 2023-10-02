import sys
sys.setrecursionlimit(10000)

# n-Queen이 가능한지 판별하는 함수
def nQueen(a):
    for i in range(a):
        # 이미 사용된 열이거나 대각선에 겹치는게 있다면 return
        if visited[a] == visited[i] or abs(visited[a] - visited[i]) == a - i:
            return
    return True


# 백트래킹
def backtracking(a):
    global res

    # 조건 달성시
    if a == n:
        res += 1
        return

    for i in range(n):
        # 몇 번째 열을 사용했는지 표시
        visited[a] = i
        
        # 만약 열이나 대각선에 겹치는게 없다면 재귀(가지치기)
        if nQueen(a):
            backtracking(a + 1)

n = int(input())
# 열을 파악하기 위한 visited
visited = [0] * n
res = 0

# 0,0 부터 시작
backtracking(0)
print(res)