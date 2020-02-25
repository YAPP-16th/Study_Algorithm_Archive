arrangement = list(str(input()))

result = 0
stick = 0

for i in range(0, len(arrangement)):

    if arrangement[i] == "(":
        stick += 1
    else:
        if arrangement[i-1] == "(":
            stick -= 1
            result += stick
        else:
            stick -= 1
            result += 1

print(result)