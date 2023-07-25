T = int(input())

for i in range(T):
    n = int(input())
    pairs = []      #빈 list 생성
    for a in range(1, 13):
        for b in range(a + 1, 13):
            if a + b == n:
                pairs.append((a, b))

    if pairs:
        string = ", ".join([f"{x} {y}" for x, y in pairs]) 
        #join 함수를 사용해 x,y 결과값이 새로 생길 때마다 , 붙이기
        print(f"Pairs for {n}: {string}")
    else:
        print(f"Pairs for {n}:")