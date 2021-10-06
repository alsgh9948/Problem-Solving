from sys import stdin
n,m,h = map(int, stdin.readline().strip().split())

ladder = [[False]*n for _ in range(h)]

for _ in range(m):
    x,y = map(int, stdin.readline().strip().split())

    ladder[x-1][y-1] = True

ladder_candidate = []

ans = 4
for i in range(h):
    for j in range(n):
        if not ladder[i][j]:
            ladder_candidate.append((i,j))

def insert_ladder(idx,cnt):
    global ans
    if cnt >= ans:
        return
    if simul():
        ans = cnt
        return
    if cnt == 3:
        return
    for i in range(idx, len(ladder_candidate)):
        x,y = ladder_candidate[i]
        if y > 0 and ladder[x][y-1]:
            continue
        if y < n-1 and ladder[x][y+1]:
            continue
        ladder[x][y] = True

        insert_ladder(i+1,cnt+1)
        ladder[x][y] = False

def simul():
    for sy in range(n):
        x = 0
        y = sy
        while x < h:
            ny = y
            if y-1 >= 0:
                if ladder[x][y-1]:
                    ny=y-1
            if y+1 < n:
                if ladder[x][y]:
                    ny=y+1
            x+=1
            y=ny
        if sy != y:
            return False
    return True

insert_ladder(0,0)
print(-1 if ans == 4 else ans)