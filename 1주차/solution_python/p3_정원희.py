a = int(input())

def count(a):
    answer =0
    for i in range(1,a+1):
        answer+= len(str(i))
    return answer
print(count(a))
