total_weight = int(input())

# 5kg와 3kg의 봉지 개수 계산
count = 0

# 최소 자루개수를 만들기 위해서는 5kg짜리를 최대한 이용해야 함으로 5를 기준으로 잡는다.
while total_weight != 0:
    if total_weight < 0:
        count = -1
        break

    # 5로 나눠지지 않으면 3만큼 들어야 함으로 우선 3을 한번만 빼준다
    if total_weight % 5 != 0:
        total_weight -= 3
        count += 1

    # 5로 나눠지면 5를 빼준다.
    elif total_weight % 5 == 0:
        total_weight -= 5
        count += 1

print(count)