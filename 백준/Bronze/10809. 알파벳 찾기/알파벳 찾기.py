word_s = list(input())

#유니코드 기준으로 소문자 a~z 는 정수로 97~122까지 이다.
for i in range(97,123):
    #chr은 정수를 유니코드로 돌려줌
    if chr(i) in word_s:
        print(word_s.index(chr(i)), end = ' ')
    else :
        print('-1', end = " ")