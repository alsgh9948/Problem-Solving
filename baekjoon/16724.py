from sys import stdin

input = stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m = map(int, input().split())
board = [input().strip() for _ in range(n)]
dir = {
    'U':0,'R':1,'D':2,'L':3
}

visited = [[0]*m for _ in range(n)]
visited_num = 0
def solv():

    answer = 0
    for sx in range(n):
        for sy in range(m):
            if not visited[sx][sy]:
                answer += simul(sx,sy)
    print(answer)

def simul(sx,sy):
    global visited, visited_num
    visited_num += 1

    x,y = sx,sy
    while True:
        if visited[x][y] != 0 and visited[x][y] != visited_num:
            return 0
        elif visited[x][y] == visited_num:
            return 1
        visited[x][y] = visited_num

        d = board[x][y]
        x += dx[dir[d]]
        y += dy[dir[d]]

solv()