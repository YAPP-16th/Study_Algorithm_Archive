T=int(input())
# 출력 결과 Array에 담는 공간
resultArray = []

# 함수 정의 (재귀 함수) n > 3으로 적용
def plusLogic(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return plusLogic(num-1) + plusLogic(num-2) + plusLogic(num-3)

# input을 받고 그에 따른 함수 호출 후 값 저장
for i in range(0, T):
    n=int(input())
    resultArray.append(plusLogic(n))

for j in resultArray:
    print(j)