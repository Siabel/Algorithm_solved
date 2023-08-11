arrays = []
array_len = []
result = []

for _ in range(5):
    arr = list(map(str, input()))
    arrays.append(arr)
    array_len.append(len(arr))

for j in range(15):
    for i in range(5):
        if j < array_len[i]:
            result.append(arrays[i][j])

a = "".join(result)
print(a)