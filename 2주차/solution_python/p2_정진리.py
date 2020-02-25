n = int(input())

dp = [0 for i in range(0, n+1)]

for i in range(1, n+1):

    # 모든 값의 초기화! 1+1+1+1+1....와 min 값을 구하기 위함
    
    dp[i] = i

    for j in range(1, i):
        # 커버리는 순간 i-j*j가 음수가 되버린다.
        if j*j > i:
            break
        dp[i] = min(dp[i], dp[i-j*j]+1)

print(dp[n])