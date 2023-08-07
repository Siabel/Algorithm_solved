import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

K = int(input())

for _ in range(K):
    sum = 0
    start_x,start_y,end_x,end_y = map(int,input().split())

    # 입력받은 좌표에서 값을 추출해 전부 더하기
    for row in range(start_x-1, end_x):
        for col in range(start_y-1, end_y):
            sum += arr[row][col]
    print(sum)