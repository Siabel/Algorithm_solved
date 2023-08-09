T = int(input())

for test_case in range(1, T + 1):
    bracket = input().strip()
    stack = []

    for i in bracket:
        # 만약 입력받은 값이 여는 괄호이면 stack에 추가
        if i == '(':
            stack.append(i)

        # 만약 입력받은 값이 닫는 괄호이면 조건문 설정
        if i == ')':
            # stack 에 값이 있으면 여는 괄호가 있다는 뜻이니까 1개를 빼줌
            if len(stack) != 0:
                stack.pop()
            # stack 에 값이 없으면 닫는 괄호와 연동되는 것이 없다는 뜻이니
            # stack에 false 값을 넣어주고 반복문 탈출
            elif len(stack) == 0:
                stack.append("false")
                break

    # stack이 값이 남아있으면 true를 반환하는 것을 감안해서 프린트
    if stack:
        print('NO')
    else:
        print('YES')
