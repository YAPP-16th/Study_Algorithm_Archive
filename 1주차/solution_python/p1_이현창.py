E,S,M = map(int, input().split())

count = 0

while True :
    if E == 0 and S == 0 and M == 0:
        break

    E = E % 15 - 1
    S = S % 28 - 1
    M = M % 19 - 1
    count += 1

print(count)