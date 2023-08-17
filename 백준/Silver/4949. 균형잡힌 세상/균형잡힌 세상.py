# 값을 계속 받아줘야 하므로 while
while True :
    sentence = input()
    stack = []

    # 만약 입력받은 문장이 . 하나일 때 입력 종료 조건
    if sentence == "." :
        break

    # 문장 안의 값 하나씩 보기
    for i in sentence :
        # 여는 괄호를 만나면 stack에 값 넣어주고
        if i == '[' or i == '(' :
            stack.append(i)
        
        # 닫는 괄호를 만났다면
        # 닫는 대괄호일 때
        elif i == ']' :
            # stack에 값에 마지막 push 된게 대괄호 쌍이면 pop
            if stack and stack[-1] == '[' :
                stack.pop()
            # 그 외에는 균형이 맞지 않음으로 stack에 false 값을 넣어주고 탈출
            else: 
                stack.append('false')
                break
        
        # 닫는 소괄호일 때
        elif i == ')' :
            # stack에 값에 마지막 push 된게 소괄호 쌍이면 pop
            if stack and stack[-1] == '(' :
                stack.pop()
            # 그 외에는 균형이 맞지 않음으로 stack에 false 값을 넣어주고 탈출
            else :
                stack.append('false')
                break

    # stack 에서 값이 전부 나왔다면 균형이 맞았다는 뜻이니까 yes
    if not stack:
        print('yes')
    else:
        print('no')