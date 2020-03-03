import collections

nList = []
visited = []

searchList = collections.deque()
searchList.append(1)

N = int(input())
M = int(input())
 
for i in range(N+1):
    nList.append([])

for i in range(M):
    a, b = map(int, input().split())
    nList[a].append(b)
    nList[b].append(a)

print(nList)

while searchList:
    idx = searchList.popleft()
    print('idx : ', searchList, idx)
    
    visited.append(idx)
    print('visited : ', visited)
    for i in nList[idx]:
        if i not in visited and i not in searchList: # 방문하지 않았으며, searchList에 중복으로 저장이 되면 안된다. 즉, 방문한적이 있으면 넣지 않는다.
            searchList.append(i)                        
 
# 총 연결점이 5개 이지만, 그 중 하나 제거! 1번 컴퓨터는 항상 걸려있기 떄문
visited.remove(1)
print(len(visited))
