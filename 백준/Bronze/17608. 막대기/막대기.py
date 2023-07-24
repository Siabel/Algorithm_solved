import sys
input = sys.stdin.readline

N = int(input())
stick = [] # 빈 stick list 생성

for _ in range(N):
    stick_length = int(input()) #for문을 통해서 값 하나씩 입력
    stick.append(stick_length)  #list에 입력값 추가

stick.reverse() #list 뒤집기(제일 마지막에 입력받은 값쪽에서 보는거라서)
cnt = 0 # 횟수 세는용 (값 초기화)
highest = 0 # 제일 큰 길이 파악용 (값 초기화)

for i in stick: #반복문 사용해서 stick 안의 값이랑 제일 긴값 비교
    if i > highest:  #만약 highest 값보다 list 안의 값이 크면
        highest = i   #highest 값 변경
        cnt += 1 #highest 값 변경 될 때 마다 횟수 세기

print(cnt)#코드를 입력하세요.