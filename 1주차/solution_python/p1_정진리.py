# 입력 받은 E, S, M의 값
E, S, M = map(int, input().split())

# 반복 횟수
count = 1

# 입력 받은 값과 일치할 때 까지 증가
ea, sa, ma = 1,1,1

while True:
    # 각 식 범위에서 벗어나면 초기 값으로 변환
    if(ea == 16):
        ea = 1
    if(sa == 29):
        sa = 1
    if(ma == 20):
        ma = 1
    
    if(E == ea and S == sa and M == ma):
        print(count)
        break
    else:
        count += 1
        ea += 1
        sa += 1
        ma += 1