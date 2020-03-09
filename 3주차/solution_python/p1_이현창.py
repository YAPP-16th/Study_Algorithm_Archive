from collections import deque

M, N = map(int, input().split())
tomato_box = []
for _ in range(N):
    tomato_box.append(list(map(int, input().split())))

queue = deque()
for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 1:
            queue.append([i, j])

while queue:
    [i, j] = queue.popleft()

    if i > 0 and tomato_box[i - 1][j] == 0:
        queue.append([i - 1, j])
        tomato_box[i - 1][j] = tomato_box[i][j] + 1

    if i < N - 1 and tomato_box[i + 1][j] == 0:
        queue.append([i + 1, j])
        tomato_box[i + 1][j] = tomato_box[i][j] + 1

    if j > 0 and tomato_box[i][j - 1] == 0:
        queue.append([i, j - 1])
        tomato_box[i][j - 1] = tomato_box[i][j] + 1

    if j < M - 1 and tomato_box[i][j + 1] == 0:
        queue.append([i, j + 1])
        tomato_box[i][j + 1] = tomato_box[i][j] + 1

answer = True
for row in tomato_box:
    if 0 in row:
        print(-1)
        answer = False
        break

if answer:
    day = 0
    for row in tomato_box:
        day = max(day, max(row))
    print(day - 1)