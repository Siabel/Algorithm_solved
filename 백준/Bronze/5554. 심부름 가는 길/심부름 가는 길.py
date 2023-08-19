total_time = 0
for _ in range(4):
    total_time += int(input())

minute = total_time // 60
second = total_time % 60

print(minute)
print(second)