word = input()
word = [n for n in word]

word.sort(reverse = True)
word = "".join(word)

print(word)