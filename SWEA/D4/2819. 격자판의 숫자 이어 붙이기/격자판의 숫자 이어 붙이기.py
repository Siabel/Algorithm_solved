dx = [1,-1,0,0]
dy = [0,0,1,-1]

def arr_make(y, x, number):
    # 문자열 길이가 7이 되면 재귀 종료
    if len(number) == 7:
        result.add(number)
        return
    
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if 0 <= nx < 4 and 0 <= ny < 4:
            arr_make(ny, nx, number + map[ny][nx])


T = int(input())

for test_case in range(1, T + 1):
    # 서로 다른 수를 합치기 위해서-> 문자열을 만들기 위해서
    # int 값이 아닌 str로 받아주기
    map = [input().split() for _ in range(4)]

    # 중복되는 문자열을 제거하기 위해 set로 결과값 받기
    result = set()

    #시작 지점 == 모두 봐야함
    for i in range(4):
        for j in range(4):
            arr_make(i, j, map[i][j])

    print(f'#{test_case}', len(result))