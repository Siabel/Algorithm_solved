from collections import deque

n = int(input())

card = deque([i + 1 for i in range(n)])

while card:
    if len(card) == 1:
        print(*card)
        break
    
    card.popleft()
    n2 = card.popleft()
    
    card.append(n2)