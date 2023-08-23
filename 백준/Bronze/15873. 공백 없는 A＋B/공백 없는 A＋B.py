arr = input()

if len(arr) == 2:
   a, b = arr[0], arr[1]
elif len(arr) == 3:
   if arr[1] == '0':
      a, b = arr[:2], arr[2]
   else:
      a, b = arr[0], arr[1:]
elif len(arr) == 4:
   a, b = arr[:2], arr[2:]

a, b = int(a), int(b)

print(a + b)