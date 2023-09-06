n, m = map(int, input().split())
col = list(map(int, input().split()))
row = list(map(int, input().split()))

for i in range(n) :
    tmp = []
    x = col[i]
    for j in range(m) :
        if x == row[j] :	# 같으면
            x = 0	# 노란색 꽃
            tmp.append(x)
        else :	# 다르면
            x = 1	# 빨간색 꽃
            tmp.append(x)     
    row = tmp	# tmp에 저장된 값을 M에 저장

print(row[-1])	# 맨 마지막에 심어진 꽃의 색을 출력
