computer_num = int(input())
network_num = int(input())

graph = {i+1 : [] for i in range(computer_num)}
for i in range(network_num) :
    x, y = list(map(int, input().split(' ')))

    graph[x].append(y)
    graph[y].append(x)

stack = [1]
visited = []
while stack :

    current_node = stack.pop()

    if current_node not in visited :
        visited.append(current_node)

    for node in graph[current_node] :
        if node not in visited :
            stack.append(node)

print(len(visited) - 1)