import sys
input = sys.stdin.readline

N = int(input())
dictionary = {}

for _ in range(N):
    card, number = input().split()
    number = int(number)
    
    dictionary[card] = dictionary[card] + number if card in dictionary else number

if 5 in dictionary.values():
    print('YES')
else:
    print('NO')