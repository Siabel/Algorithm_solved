A = int(input())
B = int(input())

B_one = B % 10
B_ten = (B % 100) // 10
B_hund = B // 100

print(B_one * A, B_ten * A, B_hund * A, B * A, sep = "\n")