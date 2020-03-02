from collections import deque


def next_pos(pos):
    for v in vector:
        ny = pos[0] + v[0]
        nx = pos[1] + v[1]

        if not (0 <= ny < n and 0 <= nx < m):
            continue
        elif tomato_box[ny][nx] == 0:
            yield ny, nx


def solve():
    total_days = -1
    global raw_tomato

    elements_at_each_round = len(queue)
    while elements_at_each_round > 0:
        for _ in range(elements_at_each_round):
            for v in next_pos(queue.popleft()):
                ny, nx = v
                tomato_box[ny][nx] = 1
                queue.append((ny, nx))
                raw_tomato -= 1

        total_days += 1
        elements_at_each_round = len(queue)

    if raw_tomato != 0:
        return -1
    else:
        return total_days


m, n = map(int, input().split())

vector = ((1, 0), (0, 1), (-1, 0), (0, -1))
queue = deque()
tomato_box = []
raw_tomato = 0

for y in range(n):
    tomato_box += [[]]
    for x, val in enumerate(map(int, input().split())):
        if val == '1':
            queue.append((y, x))
        elif val == '0':
            raw_tomato += 1

        tomato_box[y].append(int(val))

print(solve())
