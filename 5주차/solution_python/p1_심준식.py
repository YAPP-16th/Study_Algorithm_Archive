def check(row) :
    for i in range(row):
        if result[row] == result[i] :
            return False
        if abs(result[row] - result[i]) == row - i :
            return False
    return True

def dfs(row):
    global answer

    if row == N:
        answer += 1
    else :
        for i in range(N):
            result[row] = i
            if check(row) :
                dfs(row+1)

N = int(input())

result = [0] * N
answer = 0
dfs(0)
print(answer)