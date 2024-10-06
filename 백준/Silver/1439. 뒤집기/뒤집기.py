n = str(input())
cnt_0 = 0
cnt_1 = 0

flag = ''
for i in n:
    if i == '0' and flag != '0':
        cnt_0 += 1
        flag = '0'
        
    elif i == '1' and flag != '1':
        cnt_1 += 1
        flag = '1'
        
print(min(cnt_0, cnt_1))