import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
xor = A

if C % 2 == 1:
    xor = xor ^ B

print(xor)
