def is_palindrome(word):
    word = str(word)
    tmp = word[::-1]
    if word == tmp:
        return 'yes'
    else:
        return 'no'
    
while True:
    arr = input()
    if arr == '0':
        break
    else:
        print(is_palindrome(arr))