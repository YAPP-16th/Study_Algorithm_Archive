N, K = list(map(int, input().split(' ')))

lst = [i for i in range(1, N+1)]

result = []
idx = 0

while True:
    if not lst:
        break

    idx = (idx + K - 1) % len(lst)
    result.append(str(lst.pop(idx)))

print("<{}>".format(", ".join(result)))
