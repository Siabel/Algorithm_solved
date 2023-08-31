dial = {
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z']
}

word = list(input().upper())  # Convert input to uppercase to handle lowercase letters
res = 0

for i in word:
    for key, letters in dial.items():
        if i in letters:
            res += (int(key) + 1)

print(res)
