n, k = map(int, input().split())

table = [str(no) for no in range(1, n + 1)]
result = []

idx = k - 1
length = len(table)
while length > 0:
    if idx >= length:
        idx %= length

    result.append(table[idx])
    table.remove(table[idx])

    idx += k - 1
    length = len(table)

print(f"<{', '.join(result)}>")



