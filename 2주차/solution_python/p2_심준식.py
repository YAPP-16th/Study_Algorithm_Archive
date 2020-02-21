N = int(input())

dp = [i for i in range(N+1)]

for i in range(4,N+1) :
    for j in range(2,int(i**(1/2))+1) :
        dp[i] = min(dp[i], dp[i-j*j]+1)

print(dp[N])
