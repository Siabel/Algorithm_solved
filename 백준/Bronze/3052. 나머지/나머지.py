remain = set()

for _ in range(10):
    A = int(input())
    
    remain.add(A % 42)

print(len(remain))