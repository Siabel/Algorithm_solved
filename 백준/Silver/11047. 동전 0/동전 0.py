# 그리디 알고리즘 문제!
N, K = map(int, input().split())
coin_lst = []
count = 0

# 동전의 가치를 list에 추가시킨다.
for _ in range(N):
   coin_price = int(input())
   coin_lst.append(coin_price)

coin_lst.reverse()

# 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
for coin in coin_lst:
   # 최대 금액이 동전 가치로 나눠지면 그 몫만큼 동전을 줄 수 있다.
   count += K // coin 
   # 그 나눠준 금액만큼 제외하기 위해서는 나머지를 돌려준다.
   K %= coin

print(count)