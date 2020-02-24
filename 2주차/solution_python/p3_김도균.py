
n,k = map(int,input().split())
li = []

for num in range(1, n+1):
    li.append(num)

print("<", end="")
for i in range(1, n+1):
    for j in range(1, k):
        li.append(li.pop(0))
    print(li.pop(0),end="")
    print(", ", end="")
    if len(li) == 1:
        print(li.pop(0), end="")
        break
print(">")
