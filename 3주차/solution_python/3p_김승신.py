n = int(input())
e = int(input())

groups = [{uid} for uid in range(0, n + 1)]
for _ in range(e):
    v1, v2 = map(int, input().split())
    groups[v1].update(groups[v2])
    for v in groups[v1]:
        groups[v] = groups[v1]

print(len(groups[1]) - 1)
