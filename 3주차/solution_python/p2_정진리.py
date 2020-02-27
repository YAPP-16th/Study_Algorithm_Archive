# 미로 찾기 문제 bfs

import sys
import collections

input = sys.stdin.readline
N, M = map(int, input().split())

nList = []

searchList = collections.deque()
# 시작 점
searchList.append((0, 0))

for i in range(N):
    nList.append(list(input()))
    nList[i].pop()

    for j in range(M):
        nList[i][j] = int(nList[i][j])

count = 1

while searchList:

    a = [0, 0, -1, 1]
    b = [1, -1, 0, 0]

    popList = searchList.popleft()

    x = popList[0]
    y = popList[1]

    # print('popList : ', x, y)
    for i in range(0, 4):

        xx = x + a[i]
        yy = y + b[i]
        
        # print('check : ', xx, yy, nList[xx][yy], count)
        # 기본적 예외처리 + 0,0 제외 + 1이 아니면 이미 값이 있으므로 제외 + (N-1, M-1)이 1이 아니면 제외
        if (xx < 0 or yy < 0 or xx >= N or yy >= M or nList[xx][yy] == 0) or (xx == 0 and yy == 0) or nList[xx][yy] != 1 or nList[N-1][M-1] != 1:
            continue

        nList[xx][yy] = nList[x][y] + 1

        searchList.append((xx, yy))

        count = max(nList[xx][yy], count)

    # for i in range(N):
    #     for j in range(M):
    #         print(nList[i][j], end=" ")
    #     print()
print(count)