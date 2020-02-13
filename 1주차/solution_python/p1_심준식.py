E,S,M = list(map(int, input().split(' ')))

answer = 0

while True :
    if E == 0 and S == 0 and M == 0 :
        break

    E = E % 15 - 1
    S = S % 28 - 1
    M = M % 19 - 1
    answer += 1

print(answer)