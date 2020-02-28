from collections import deque


def next_pos(pos):
    vector = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for v in vector:
        ny = pos[0] + v[0]
        nx = pos[1] + v[1]

        if (0 <= ny < n and 0 <= nx < m) and miro[ny][nx] == 1:
            yield ny, nx

    # return result

# 글로벌 변수 + 함수로 따로 빼기는 것은 메모리 초과가 일어났다.  (2)
# def bfs(steps):
#     # global min_step
#     queue.append((0, 0))
#     # min_step = 1
#     while len(queue) > 0:
#         for _ in range(len(queue)):
#             for v in next_pos(queue.popleft()):
#                 queue.append(v)
#                 if v[0] == n - 1 and v[1] == m - 1:
#                     steps += 1
#                     return steps
#         steps += 1
#     return steps

# 파이썬은 dfs 로 풀면 시간초과 난다. (1)
# def dfs(pos, steps):
#     global min_step
#     y, x = pos
#
#     if min_step <= steps:
#         return
#
#     if y == n - 1 and x == m - 1:
#         min_step = min(min_step, steps)
#         return
#
#     miro[y][x] = 0
#     for v in next_pos(pos):
#         dfs(v, steps + 1)
#     miro[y][x] = 1
#
#     return


def solve():
    # dfs((0, 0), 1)    (1)
    # return min_step   (1, 2)
    # return bfs(1)     (2)

    vector = ((1, 0), (0, 1), (-1, 0), (0, -1))
    queue = deque()

    steps = 1
    miro[0][0] = 0
    queue.append((0, 0))
    while queue:
        next_queue = deque()
        for pos in queue:
            for v in next_pos(pos):
                ny, nx = v

                if 0 <= ny < n and 0 <= nx < m and miro[ny][nx] == 1:
                    miro[ny][nx] = 0
                    next_queue.append([ny, nx])
                    if ny == n - 1 and nx == m - 1:
                        return steps + 1

        steps += 1
        queue = next_queue

    return steps


n, m = map(int, input().split())
miro = []
# min_step = n * m (1)

for _ in range(n):
    miro.append(list(map(int, input())))

print(solve())
