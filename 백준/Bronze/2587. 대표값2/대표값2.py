num_lst = []

for _ in range(5):
    num = int(input())
    num_lst.append(num)

# 평균값 구하기
sum = 0

for i in num_lst:
    sum += i

average = sum // 5
print(average)

# 중앙값 구하기
# 1. 버블 정렬 (연습 + 공부)
# for i in range(len(num_lst)-1, 0, -1):
#     for j in range(0, i):
#         if num_lst[j] > num_lst[j+1]:
#             num_lst[j], num_lst[j+1] = num_lst[j+1], num_lst[j]

# middle = num_lst[2]
# print(middle[2])

# 2. 편하게...
middle = sorted(num_lst)
print(middle[2])