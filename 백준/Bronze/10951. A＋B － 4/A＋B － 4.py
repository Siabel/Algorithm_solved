#EOF 에 대해 알아보는 문제
while True:
    #try/except : 아무것도 입력 안하면 탈출
    try:
        A, B = map(int,input().split())
        print(A+B)
    except: #EOFError 발생 - 입력을 안해서 Error가 나서 break
        break