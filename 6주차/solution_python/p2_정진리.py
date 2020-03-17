N, M = map(int,input().split())

nList = []
sStr = ""
cnt = 0

for i in range(N):
    nList.append(list(input()))

for i in range(M):
    A, T, G, C = 0, 0, 0, 0
    for j in range(N):
    
        if nList[j][i] == "A":
            A += 1
        elif nList[j][i] == "T":
            T += 1
        elif nList[j][i] == "G":
            G += 1
        elif nList[j][i] == "C":
            C += 1
    
    if A >= C and A >= G and A >= T:
        sStr += "A"
    elif C >= G and C >= T:
        sStr += "C"
    elif G >= T:
        sStr += "G"
    else:
        sStr += "T"
        
print(sStr)

for i in range(N):
    for j in range(M):
        if nList[i][j] != sStr[j]:
            cnt += 1

print(cnt)