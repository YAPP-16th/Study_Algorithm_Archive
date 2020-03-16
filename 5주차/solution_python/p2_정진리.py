def dfs(selected, v, k):

    global max_cnt
    a = [0, 0, -1, 1]
    b = [1, -1, 0, 0]

    for x in range(0, 4):
        i = v[0] + a[x]
        j = v[1] + b[x]

        # i, j는 음수의 값을 가질 수 없으며, R-1 C-1을 넘을 수 없다. 또한 중복배열에 포함하지 않아야 한다!
        if 0 <= i <= R-1 and 0 <= j <= C-1 and not(selected[ord(nList[i][j])-65]):

            selected[ord(nList[i][j])-65] = True
            
            # 재귀를 탔을 때만, selected를 첨부하여, 중복되지 않게 한다.
            dfs(selected, [i, j], k + 1)

            # 재귀를 벗어나면 selected를 초기화 하여, 다음번이 진행할 수 있도록 한다.
            selected[ord(nList[i][j])-65] = False
    if k > max_cnt:
        max_cnt = k

R, C = map(int, input().split())
max_cnt = 1
nList = []

# 리스트로 하면 시간초과 남
nList = [input() for _ in range(R)]

overList = [False]*26

overList[ord(nList[0][0])-65] = True
dfs(overList, [0, 0], 1)

print(max_cnt)