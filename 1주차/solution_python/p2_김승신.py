memo = [0, 1, 2, 4] + [0 for _ in range(9)]
for idx in range(4, 12):
    memo[idx] = memo[idx - 3] + memo[idx - 2] + memo[idx - 1]


for _ in range(int(input())):
    n = int(input())
    print(memo[n])
