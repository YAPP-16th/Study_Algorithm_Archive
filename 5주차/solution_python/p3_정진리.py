# 그리디 알고리즘 사용하는 문제

# 1. sorting
# 2. cnt+1 < a[i]
# 3. 아니면 cnt += a[i]
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
print(a)
cnt = 0

for i in range(0, n) :
    print(cnt+1, a[i])
    if cnt+1 < a[i]:
        break
    cnt += a[i]

print(cnt+1)