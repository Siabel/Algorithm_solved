import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
money_lst = deque()

for _ in range(n):
    money = int(input())
    if money == 0 and money_lst:
        money_lst.pop()
    else:
        money_lst.append(money)

print(sum(money_lst))