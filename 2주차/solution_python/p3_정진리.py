# 1 2 3 4 5 6 7 -> 3, 6, 2, 7, 5, 1, 4 == 2
# 1 2 4 5 6 7 == 4
# 1 2 4 5 7 == 1
# 1 4 5 7 == 3
# 1 4 5 == 2
# 1 4 == 0
# 1 == 1

n, k = map(int, input().split())

nList = []

mList = []
cnt = k-1

for i in range(1, n+1):
    nList.append(i)

while True:
    mList.append(nList[cnt])
    nList.pop(cnt)

    # nList pop all
    if len(nList) == 0:
        break

    # 7인 경우
    # -> 2 4 1 3 2 0 1
    
    cnt = (cnt+k-1) % len(nList)

# print(mList)
    
for i in mList:
    if i == mList[0]:
        print("<" , end="")
    

    if i == mList[len(mList)-1]:
        print(i, end="")
    else:
        print(i, ",", sep="", end=" ")
print(">", end="")