A, B = input().split()

new_A = "".join(list(reversed(A)))
new_B = "".join(list(reversed(B)))

if new_A > new_B:
    print(new_A)
else:
    print(new_B)
