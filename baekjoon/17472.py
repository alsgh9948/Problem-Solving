from sys import stdin
from collections import deque
from itertools import combinations

dx = [-1,1,0,0]
dy = [0,0,-1,1]
INF = 9876543210

input = stdin.readline
n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
edge_list = [[],[]]
dist_board = []
bridge = []

def solv():
    answer = INF
    set_area()
    set_dist_board()
    set_bridge()
    visited = [0]*len(dist_board)
    visited_num = 1
    for cnt in range(1,len(dist_board)-2):
        for comb in combinations(bridge,cnt):
            select = [[False]*len(dist_board) for _ in range(len(dist_board))]
            total = 0
            for x,y,length in comb:
                select[x][y] = True
                select[y][x] = True
                total += length
            visited[2] = visited_num
            check_dfs(select,visited,visited_num,2)
            if visited.count(visited_num) == len(dist_board)-2:
                answer = min(answer, total)
            visited_num += 1
    print(answer if answer != INF else -1)

def set_bridge():
    global bridge
    for now in range(2,len(dist_board)-1):
        for nxt in range(now+1, len(dist_board)):
            if dist_board[now][nxt] != INF:
                bridge.append((now,nxt,dist_board[now][nxt]))
def check_dfs(select,visited,visited_num,now):
    for nxt in range(2,len(select)):
        if select[now][nxt] and visited[nxt] != visited_num:
            visited[nxt] = visited_num
            check_dfs(select,visited,visited_num,nxt)

def set_dist_board():
    for edges in edge_list:
        for x,y in edges:
            num = board[x][y]
            for d in range(4):
                dist,dest = set_dist_dfs(x,y,d,0,num)
                if dist > 1:
                    dist_board[num][dest] = min(dist,dist_board[num][dest])
def set_dist_dfs(x,y,d,cnt,num):
    x += dx[d]
    y += dy[d]
    if point_validator(x,y):
        if board[x][y] == num:
            return -1,-1
        elif board[x][y] == 0:
            return set_dist_dfs(x,y,d,cnt+1,num)
        else:
            return cnt, board[x][y]
    return -1,-1

def set_area():
    global board,dist_board
    num = 2
    for x in range(n):
        for y in range(m):
            if board[x][y] == 1:
                set_area_bfs(x,y,num)
                num += 1
    dist_board = [[INF]*num for _ in range(num)]
def set_area_bfs(sx,sy,num):
    global board,edge_list
    q = deque([(sx,sy)])
    board[sx][sy] = num
    edge = []
    while q:
        x,y = q.pop()
        edge_flag = False
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                if board[nx][ny] == 0:
                    edge_flag = True
                elif board[nx][ny] != num:
                    board[nx][ny] = num
                    q.appendleft((nx,ny))
        if edge_flag:
            edge.append((x,y))
    edge_list.append(edge)
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True

solv()