def ascending():
    global result
    if arr == [1, 2, 3, 4, 5, 6, 7, 8]:
        result = 'ascending'

def descending():
    global result
    if arr == [8, 7, 6, 5, 4, 3, 2, 1]:
        result = 'descending'

arr = list(map(int, input().split()))
result = ''
ascending()

descending()

if result == '':
    print('mixed')
else:
    print(result)