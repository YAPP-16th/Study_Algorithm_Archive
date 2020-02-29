n = int(input())

dp = [0]*(n+1)
for i in range(1, n+1):
    dp[i] = i
    j = 1
    while j*j <= i:
        if dp[i] > dp[i-j*j]+1:
            dp[i] = dp[i-j*j]+1
        j += 1
print(dp[n])
