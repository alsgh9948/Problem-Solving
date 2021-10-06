n, m = map(int, input().strip().split())

paper = [list(map(int,input().strip())) for _ in range(n)]
dir_map = [[0]*m for _ in range(n)]
ans = -1
# visited = [[False]*m for _ in range(n)]

# def select_dir(x,y,cnt):
#     global paper
#     if cnt == n*m:
#         calc_sum()
#         return
#     for i in range(x,n):
#         for j in range(y,m):
#             for d in range(1,3):
#                 dir_map[i][j] = d
#                 select_dir(i,j+1,cnt+1)
#                 dir_map[i][j] = 0
#         y = 0
#
# def calc_sum():
#     sum = 0
#     for i in range(n):
#         for j in range(m):
#             if visited[i][j]: continue
#             num = 0
#             dir = dir_map[i][j]
#             x, y = i, j
#             while x >= 0 and y >= 0 and x < n and y < m:
#                 visited[x][y] = True
#                 num += paper[x][y]
#                 x, y = calc_next_point(x,y,dir)
#                 if x == -1 or y == -1:
#                     break
#                 num *= 10
#             sum += num
#     global ans
#     ans = max(sum, ans)

def select_dir(x,y,cnt,sum):
    global dir_map

    for i in range(x,n):
        for j in range(y,m):
            if dir_map[i][j] != 0: continue
            select_dir(i,j+1,cnt+1, sum + insert_value(i,j,1))
            insert_value(i,j,1,True)

            select_dir(i,j+1,cnt+1, sum + insert_value(i,j, 2))
            insert_value(i,j,2,True)

            dir_map[i][j] = 3
            select_dir(i,j+1,cnt+1, sum + paper[i][j])
            dir_map[i][j] = 0
        y = 0

    global ans
    ans = max(sum, ans)


def insert_value(x,y,dir,clear=False):
    global dir_map
    num = 0
    while x >= 0 and y >= 0 and x < n and y < m:
        if clear:
            dir_map[x][y] = 0
        else:
            dir_map[x][y] = dir
            num += paper[x][y]
        x, y = calc_next_point(x,y,dir,clear)
        if x == -1 or y == -1:
            break
        num *= 10
    return num
def calc_next_point(x,y,d,clear):
    if d == 1:
        x += 1
        if x >= n:
            x = -1
        else:
            if clear and dir_map[x][y] != d:
                x = -1
            elif not clear and dir_map[x][y] != 0:
                x = -1
    else:
        y += 1
        if y >= m:
            y = -1
        else:
            if clear and dir_map[x][y] != d:
                y = -1
            elif not clear and dir_map[x][y] != 0:
                y = -1
    return x,y

select_dir(0,0,0,0)
print(ans)