n = int(input())

arr = list(map(int, input().split()))
stack = []
temp = []
idx = 0

while len(stack) != n:
    for i in arr:
        idx += 1

        if i == 0:
            stack.append(idx)
        else:
            for _ in range(i):
                temp.append(stack.pop())
            stack.append(idx)
            while temp:
                stack.append(temp.pop())

print(*stack)