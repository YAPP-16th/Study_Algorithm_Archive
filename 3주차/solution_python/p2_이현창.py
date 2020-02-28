row, column = map(int, input().split())
maze = []
way = []
Q = []
for j in range(row):
    maze.append([])
    way.append([])
    for i in input():
        if i == '0':
            maze[j].append(0)
            way[j].append(2)
        else:
            maze[j].append(1)
            way[j].append(0)


def re(y, x):
    way[y][x] = 1

    if x > 0:
        if way[y][x - 1] == 0 and maze[y][x - 1] >= 1:
            maze[y][x - 1] = maze[y][x] + 1
            Q.append([y, x - 1])
    if y > 0:
        if way[y - 1][x] == 0 and maze[y - 1][x] >= 1:
            maze[y - 1][x] = maze[y][x] + 1
            Q.append([y - 1, x])
    if x < column - 1:
        if way[y][x + 1] == 0 and maze[y][x + 1] >= 1:
            maze[y][x + 1] = maze[y][x] + 1
            Q.append([y, x + 1])
    if y < row - 1:
        if way[y + 1][x] == 0 and maze[y + 1][x] >= 1:
            maze[y + 1][x] = maze[y][x] + 1
            Q.append([y + 1, x])


re(0, 0)
while True:
    temp = Q[:]
    Q = []
    for y, x in temp:
        re(y, x)
    if len(Q) == 0: break

print(maze[row - 1][column - 1])