n, m = map(int, input().split())
cnt_store = int(input())
coordinate = []
result = 0

for _ in range(cnt_store):
    direction, location = map(int, input().split())
    coordinate.append([direction, location])

dong_c, dong_l = map(int, input().split())

for i in range(cnt_store):
    direct = []
    now_c = coordinate[i][0]
    now_l = coordinate[i][1]
    
    if now_c == dong_c:
        result += abs(dong_l - now_l)
    else:
        if now_c in (1, 2) and dong_c in (1, 2):
            direct.append(m + dong_l + now_l)
            direct.append(m + abs(n - dong_l) + abs(n - now_l))
            result += min(direct)
        elif now_c in (3, 4) and dong_c in (3, 4):
            direct.append(n + dong_l + now_l)
            direct.append(n + abs(m - dong_l) + abs(m - now_l))
            result += min(direct)

        else:
            if now_c == 1:
                if dong_c == 3:
                    result += now_l + dong_l
                else:  # dong_d == 4
                    result += n - now_l + dong_l
            elif now_c == 2:
                if dong_c == 3:
                    result += now_l + (m - dong_l)
                else:  # dong_d == 4
                    result += n - now_l + (m - dong_l)
            elif now_c == 3:
                if dong_c == 1:
                    result += now_l + dong_l
                else:  # dong_d == 2
                    result += m - now_l + dong_l
            else:  # now_coor == 4
                if dong_c == 1:
                    result += now_l + (n - dong_l)
                else:  # dong_d == 2
                    result += n - now_l + (m - dong_l)

print(result)
