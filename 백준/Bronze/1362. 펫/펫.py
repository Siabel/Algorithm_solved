#코드를 입력하세요.
scenario = 0

# 1. pet한테 시킬 행동
# 2. pet weight_o와 weight_w 비교

while True:
    weight_o, weight_w = map(int,input().split())
    a = 0
    if weight_o == 0 and weight_w == 0:
        break
    #0 0 입력되면 끝
    while True:
        to_do, n = input().split()
        n = int(n)
        #먹이주기
        
        if to_do == "F":
            weight_w += n
        #운동시키기 (사망하는건 이때밖에 없지않나)
        elif to_do == "E":
            weight_w -= n
            #사망...
            if weight_w <= 0:
                a = 1
        #중간출력
        elif to_do == "#" and n == 0:
            scenario += 1
            if a == 1: 
                print(f"{scenario} RIP")
            elif (weight_o * 2) > weight_w > (weight_o * 0.5):
                print(f'{scenario} :-)')
            else:
                print(f'{scenario} :-(')
            break
