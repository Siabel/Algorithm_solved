cnt = int(input())
measure = list(map(int, input().split()))

max_measure = max(measure)
min_measure = min(measure)

if max_measure != min_measure:
    number = max_measure * min_measure
else:
    number = max_measure ** 2

print(number)