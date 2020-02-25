line = input().rstrip()

count = 0
stack = []
for idx, c in enumerate(line):
    if c == '(':
        stack.append(c)
    elif line[idx - 1] == '(':
        stack.pop()
        count += len(stack)
    else:
        stack.pop()
        count += 1

print(count)