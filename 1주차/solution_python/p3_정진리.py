n = int(input())

count = 0
increase = 9

while n >= 1:
    nVar = n
    nVarCount = 1
# nVarCount 10 계수
    while nVar >= 10:
        nVar = nVar // 10
        nVarCount += 1

    n -= 1
    count += nVarCount

print(count)

# 시간초과 나는 코드..