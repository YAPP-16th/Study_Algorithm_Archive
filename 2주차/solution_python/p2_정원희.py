input = int(input())

def sum(input):
    dp = [0 for i in range(input+1)]
    square = [ i*i for i in range(1, 317)]
    for i in range(1,input+1):
        s = []
        for j in square:
            if j >i:
                break
            s.append(dp[i-j])
        dp[i]=min(s)+1
    return dp[input]

print(sum(input))