cnt = 0
while True:
    cnt += 1
    n0 = int(input())
    if n0 == 0 :
        break
    n1 = n0 *3
    if n1 % 2 != 0:
        n2 = (n1 + 1) // 2
        n3 = n2 * 3
        n4 = n3 // 9
        print(f"{cnt}. odd {n4}")
    else:
        n2 = n1 // 2
        n3 = n2 * 3
        n4 = n3 // 9
        print(f"{cnt}. even {n4}")
