direction = ['N','E','S','W']
first = 0

for _ in range(10):
    order = int(input())

    if order == 1:
        first += 1
    elif order == 2:
        first += 2
    elif order == 3:
        first += 3

print(direction[first % 4])