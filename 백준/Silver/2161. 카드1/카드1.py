n = int(input())
arr = [x+1 for x in range(n)]

queue = []

while len(arr) != 1:
    # 버린 첫 번째 카드
    n1 = arr.pop(0)
    queue.append(n1)

    # 그 다음 카드 밑으로 옮기기
    n2 = arr.pop(0)
    arr.append(n2)

queue.append(arr.pop())
print(*queue)