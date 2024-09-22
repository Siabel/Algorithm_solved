import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

# 산술평균
sum = 0

for num in arr:
    sum += num
print(round(sum / n))

# 중앙값
mid = n // 2
sorted_arr = sorted(arr)
mid = sorted_arr[mid]
print(mid)

# 최빈값
freq_lst = [0 for _ in range(n)]
 
for i in range(1, n):
    if sorted_arr[i - 1] == sorted_arr[i]:
        freq_lst[i] = freq_lst[i-1] + 1
max_freq = max(freq_lst)
 
max_freq_list = []
for i in range(n):
    if freq_lst[i] == max_freq:
        max_freq_list.append(sorted_arr[i])

if n == 1:
    max_cnt_num = arr[0]
elif len(max_freq_list) == 1:
    max_cnt_num = max_freq_list[0]
else:
    max_cnt_num = max_freq_list[1]
print(max_cnt_num) # 최빈값

# 범위
range = max(arr) - min(arr)
print(range)