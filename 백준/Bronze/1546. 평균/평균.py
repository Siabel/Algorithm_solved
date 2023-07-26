import sys
input = sys.stdin.readline

N = int(input())
new_lst = []
average_score = 0

score_lst = list(map(int,input().split()))

high_score = max(score_lst)

for i in range(N):
    new_score = float(score_lst[i] / high_score * 100)
    average_score += new_score / N

print(average_score)