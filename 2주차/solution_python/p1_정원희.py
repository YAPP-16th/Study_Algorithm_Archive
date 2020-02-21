input = str(input())

def laser(input):
    stack = []
    sign = 0
    answer =0
    for i in list(input):
        if i == "(":
            stack.append(1)
            answer+=1
            sign = 1
        else:
            stack.pop()
            if sign != 0 :
                answer += len(stack)-1
            sign =0

    return answer
print(laser(input))
