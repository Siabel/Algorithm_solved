lst = []
for _ in range(5):
    sock = int(input())
    if not sock in lst:
        lst.append(sock)
    else:
        lst.remove(sock)

print(*lst)
