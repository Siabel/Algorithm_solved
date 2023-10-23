n = int(input())
word = list(input())
for _ in range(n - 1):
    words = input()
    for j in range(len(words)):
        if word[j] != words[j]:
            word[j] = "?"

print("".join(word))