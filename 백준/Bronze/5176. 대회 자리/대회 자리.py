import sys
input = sys.stdin.readline

test_num = int(input()) #확인해볼 test횟수 구하기

for _ in range(test_num):
    P,M = map(int,input().split())
    lst = [0 for _ in range(M)]
    for i in range(P):
        seat = int(input())
        lst[seat-1] += 1
    
    count_list = []

    for j in range(len(lst)):
        if lst[j] > 1:
            count_list.append(lst[j]-1)
    print(sum(count_list[:M]))