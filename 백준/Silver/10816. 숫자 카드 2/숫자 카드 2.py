import sys
input = sys.stdin.readline

n = int(input())
n_lst = map(int, input().split())
m = int(input())
m_lst = map(int, input().split())

dictionary = dict()

for i in n_lst:
    if i in dictionary.keys():
        dictionary[i] += 1
    else:
        dictionary[i] = 1

for j in m_lst:
    if j in dictionary.keys():
        print(dictionary[j], end=' ')
    else:
        print(0, end=' ')