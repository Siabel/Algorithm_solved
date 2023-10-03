n = int(input())
arr = input()
num_lst = [0] * n	

for i in range(n):
    num_lst[i] = int(input())

stack = []

for i in arr :					
    if i.isalpha():
        stack.append(num_lst[ord(i)-ord('A')])
    else :
        n2 = stack.pop()
        n1 = stack.pop()

        if i =='+' :
            stack.append(n1 + n2)
        elif i == '-' :
            stack.append(n1 - n2)
        elif i == '*' :
            stack.append(n1 * n2)
        elif i == '/' :
            stack.append(n1 / n2)

print("{:.2f}".format(stack[0]))
