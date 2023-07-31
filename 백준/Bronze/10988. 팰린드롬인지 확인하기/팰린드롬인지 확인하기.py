word = list(map(str, input()))
drow = list(reversed(word))

if word == drow:
    print("1")
else:
    print("0")