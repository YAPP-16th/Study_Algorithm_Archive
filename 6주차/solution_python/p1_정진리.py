cnt = 1
while True:
    L, P, V = map(int, input().split())
    if 1 < L < P < V:
        quotient = V // P
        remainder = V % P
        if L <= remainder:
            print("Case %d: %d" %(cnt, L*(quotient+1)))
        else:
            print("Case %d: %d" %(cnt, L*quotient+remainder))
        cnt += 1
    else:
        break
