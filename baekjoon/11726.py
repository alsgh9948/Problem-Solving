n = int(input())

def solv(a,b,now):
    if now > n:
        return b
    else:
        return solv(b,a+b,now+1)

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    print(solv(1,2,3)%10007)