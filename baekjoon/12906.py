from collections import deque

a=b=c=-1
for i in range(3):
    input_str = input().strip()
    num = 0
    if input_str != '0':
        str = input_str.split()[1]
        for ch in str:
            if ch == 'A':
                num += 1
            elif ch == 'B':
                num += 2
            elif ch == 'C':
                num += 3
            num *= 10
    if a == -1:
        a = num//10
    elif b == -1:
        b = num//10
    else:
        c = num//10
def bfs():
    visited = set([])
    visited.add((a,b,c))

    q = deque()
    q.appendleft((a,b,c,0))

    while q:
        x,y,z,cnt = q.pop()
        if ans_check(x,1) and ans_check(y,2) and ans_check(z,3):
            return cnt

        if x != 0:
            xt = x%10
            xx = x // 10

            if not (xx,y*10+xt,z) in visited:
                visited.add((xx,y*10+xt,z))
                q.appendleft((xx,y*10+xt,z,cnt+1))

            if not (xx,y,z*10+xt) in visited:
                visited.add((xx,y,z*10+xt))
                q.appendleft((xx,y,z*10+xt,cnt+1))

        if y != 0:
            yt = y%10
            yy = y // 10

            if not (x*10+yt,yy,z) in visited:
                visited.add((x*10+yt,yy,z))
                q.appendleft((x*10+yt,yy,z,cnt+1))

            if not (x,yy,z*10+yt) in visited:
                visited.add((x,yy,z*10+yt))
                q.appendleft((x,yy,z*10+yt,cnt+1))

        if z != 0:
            zt = z%10
            zz = z // 10

            if not (x*10+zt,y,zz) in visited:
                visited.add((x*10+zt,y,zz))
                q.appendleft((x*10+zt,y,zz,cnt+1))

            if not (x,y*10+zt,z) in visited:
                visited.add((x,y*10+zt,zz))
                q.appendleft((x,y*10+zt,zz,cnt+1))
def ans_check(num, target):
    while num != 0:
        tmp = num%10
        if tmp != target:
            return False
        num //= 10
    return True

print(bfs())