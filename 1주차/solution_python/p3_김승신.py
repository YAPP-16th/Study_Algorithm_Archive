n           = int(input())
digit       = 0
temp        = n
answer      = 0
increase    = 9

while temp > 0:
    temp //= 10
    digit += 1

temp = 1
while temp < digit:
    answer += increase * temp
    increase *= 10
    temp += 1

answer += (n - 10 ** (digit - 1) + 1) * digit
print(answer)
