N = int(input())
count = {}
lst = []

for _ in range(N):
    num = int(input())
    lst.append(num)

for i in lst:
    try: count[i] += 1
    except: count[i] = 1

most_count = max(list(count.values()))
value = [k for k, v in count.items() if v == most_count]

if len(value) != 1 :
    print(min(value))
else:
    print(*value)