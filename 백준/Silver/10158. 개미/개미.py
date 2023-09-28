w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

w_lst = [i for i in range(w)]
h_lst = [i for i in range(h)]

for j in range(w, 0, -1):
    w_lst.append(j)

for j in range(h, 0, -1):
    h_lst.append(j)

x = (t + x) % len(w_lst)
y = (t + y) % len(h_lst)

print(w_lst[x], h_lst[y])