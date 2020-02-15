N = int(input())
answer = 0
N_length = len(str(N))

for i in range(1,N_length+1) :
    if i == N_length :
        answer += i * (N - 10**(i-1) + 1)
    else :
        answer += i * (int('9'*i) - 10**(i-1) + 1)

print(answer)
