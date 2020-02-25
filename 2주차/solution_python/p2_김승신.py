def solve():
    for idx in range(1, n + 1):
        if memo[idx] == 1:
            continue

        memo[idx] = idx
        jdx = 1
        while jdx * jdx <= idx:
            memo[idx] = min(memo[idx], 1 + memo[idx - jdx * jdx])
            if memo[idx] <= 2:
                break
            jdx += 1
    return memo[n]


n = int(input())
memo = [0 for _ in range(n + 1)]

_idx = 1
while _idx * _idx <= n:
    memo[_idx * _idx] = 1
    _idx += 1

if memo[n] == 1:
    print(1)
else:
    print(solve())
