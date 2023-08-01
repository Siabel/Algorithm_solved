#Test case의 개수를 받아주고
T = int(input()) 

#ord 전체의 list를 받아준다
ord_lst = [_ for _ in range(65,91)] 

# Test case 수 만큼 반복해야하니 반복문 돌려주고
for _ in range(T):
    #새로운 test를 할때마다 값을 더해줄 list를 만든다
    empty_lst = []
    # 새로운 test할 값 받아주고
    word_lst = list(map(ord,input()))
    # test할 값이랑 전체 ord list랑 비교해준다
    for i in range(len(ord_lst)):
        #만약 word_lst 안에 ord_lst 값이 없을 때에
        if ord_lst[i] not in word_lst:
            # 그 값을 empty list에 더해준다
            empty_lst.append(ord_lst[i])
    #empty list에 있는 값들을 다 더해준다          
    print(sum(empty_lst))

