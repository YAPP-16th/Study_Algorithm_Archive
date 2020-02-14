T = int(input())

for i in range(T):
    n = int(input())

    a = [0 for x in range(12)]
    a[1] = 1
    a[2] = 2
    a[3] = 4

    for j in range(4,n+1):
        a[j] = a[j-1]+a[j-2]+a[j-3]

    print(a[n])
