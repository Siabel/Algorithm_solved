def min_squares(n):
    # dp[i]는 자연수 i를 제곱수들의 합으로 표현할 때의 최소 개수를 저장하는 배열
    dp = [0] + [float('inf')] * n

    # 1부터 n까지의 자연수에 대해서 최소 개수를 계산
    for i in range(1, n + 1):
        # i의 정수 제곱근을 구함
        root = int(i ** 0.5)

        # i보다 작은 제곱수들을 활용하여 최소 개수를 찾음
        for j in range(1, root + 1):
            dp[i] = min(dp[i], dp[i - j * j] + 1)

    return dp[n]


# 사용
N = int(input())
result = min_squares(N)
print(result)