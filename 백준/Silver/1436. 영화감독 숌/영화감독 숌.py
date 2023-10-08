n = int(input())

movie = []

for i in range(int(1e9)):
    if len(movie) == 10001:
        break
    if '666' in str(i):
        movie.append(i)
    else:
        continue

print(movie[n-1])