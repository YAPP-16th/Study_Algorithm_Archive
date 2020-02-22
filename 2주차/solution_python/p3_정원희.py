n, k = map(int, input().split())
s = [i for i in range(1,n+1)]
n =0
answer =[]
while len(s)>0:
    if (n+1) % k  ==0:
        answer.append(s.pop(0))
    else:
        s.append(s.pop(0))
    n +=1
answer = str(answer)
print("<"+answer[1:-1]+">")
