def year(e,s,m):
    answer =1
    a=b=c=0
    while 1 :
        if e == answer-15*a and s == answer -28*b and m == answer -19*c:
            break
        else:
            if answer%15==0:
                a +=1
            if answer%28==0:
                b +=1
            if answer%19 ==0:
                c+=1
            answer+=1

    return answer