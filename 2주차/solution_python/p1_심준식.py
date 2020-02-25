s = input()

bar = 0
total = 0

for idx, ch in enumerate(s) :
    if ch == '(' :
        bar += 1
        total += 1
    else :
        bar -= 1
        if s[idx-1] == '(':
            total += bar - 1

print(total)


# s = input()
#
# answer = 0
#
# stack = []
# s = s.replace('()', 'L')
#
# for i in s :
#
#     if i == 'L' :
#         answer += len(stack)
#
#     elif i == '(' :
#         stack.append('(')
#         answer += 1
#
#     elif i == ')' :
#         stack.pop()
#
# print(answer)
