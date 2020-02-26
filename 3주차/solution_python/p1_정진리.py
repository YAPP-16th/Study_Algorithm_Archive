# bfs 문제 너비 우선 탐색
# deque 사용! deque는 double-ended-queue 자료구조 
# append extend pop

import sys
import collections

# 기존보다 속도 증가
input = sys.stdin.readline
M, N = map(int, input().split())

zeroCount = 0
nList = []
# 토마토 리스트
tomato = collections.deque()

for i in range(N):
    nList.append(list(map(int, input().split())))
    
 
for i in range(N):
    for j in range(M):
        if nList[i][j] == 1 :
            tomato.append((i, j))
        elif nList[i][j] == 0:
            zeroCount += 1
        else:
            continue

# 다 익은 상태 경우 days
days = 1

while tomato:
 
    # 상하좌우
    a = [0, 0, 1, -1]
    b = [1, -1, 0, 0]
    
    popList = tomato.popleft()
 
    x = popList[0]
    y = popList[1]
 
    for i in range(0, 4) :
 
        nx = x + a[i]
        ny = y + b[i]
 
        # x, y 값의 오류인 경우 & 좌표 -1
        if (nx >= N or nx < 0 or ny >= M or ny < 0) or (nList[nx][ny] != 0):
            continue
        
        # 익음!
        nList[nx][ny] = nList[x][y] + 1
        tomato.append((nx, ny))
        
        days = max(nList[nx][ny], days)
        zeroCount -= 1
 
if zeroCount == 0 :
    print(days-1)
else :
    print(-1)