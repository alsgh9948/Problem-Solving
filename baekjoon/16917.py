
a,b,c,x,y = map(int,input().split())

ans = 0

if c*2 < a+b:
    ans += min(x,y)*2*c
    if x < y:
        if c*2 < b:
            ans += (y-x)*2*c
        else:
            ans += (y-x)*b
    else:
        if c*2 < a:
            ans += (x-y)*2*c
        else:
            ans += (x-y)*a
else:
    ans = a*x+b*y

print(ans)