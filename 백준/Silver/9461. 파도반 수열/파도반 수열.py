#코드를 입력하세요.
import sys
input = sys.stdin.readline

Test_number = int(input())

#Test 하기로 한 횟수만큼 P(n)의 n값 받기
for _ in range(Test_number):
    pN = int(input())

# 1. 규칙 찾아봤더니  : P(4)부터 P(n-2)랑 P(n-3) 더하면 P(4) 나옴 
# =>P(n) = P(n-3) + P(n-2)
    # P(4)부터라서 P(3)까지는 적용이 안돼서 그냥 값을 넣어줌
    lst = [1,1,1]
    # pN값은 3보다 커야하므로
    if pN >= 3:
        #index 0,1,2 값은 있으니까 3부터 시작 n값 까지(n값 이후로는 몰라도 되니까)
        for i in range(3, pN): 
            #P(n) = P(n-2) + P(n-3)
            lst.append(lst[i - 2] + lst[i - 3])
            #P(n) 값 lst에 추가해주기
    
        print(lst[pN-1])

	#pN 값이 3보다 작거나 같을 경우
    else:
        print(lst[pN-1])