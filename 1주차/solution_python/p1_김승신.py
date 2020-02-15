def mapper(idx: int, raw: int):
    if idx == 0:
        return raw % 15
    elif idx == 1:
        return raw % 28
    else:
        return raw % 19


year = 0
esm = list(map(lambda x: int(x) - 1, input().split()))
while sum(esm) != 0:
    esm = list(map(lambda enum: mapper(enum[0], enum[1] - 1), enumerate(esm)))
    year += 1

print(year + 1)


