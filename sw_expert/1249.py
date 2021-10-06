import heapq

dx = [-1,1,0,0]
dy = [0,0,-1,1]

tc = int(input())

visited = [[0]*100 for _ in range(100)]
visited_num = 0

def solv(t):
    global n,board
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]

    print('#%d %d'%(t,bfs()))
def bfs():
    global visited

    visited[0][0] = visited_num

    pq = []
    heapq.heappush(pq,(0,0,0))

    while pq:
        cnt,x,y = heapq.heappop(pq)

        x *= -1
        y *= -1
        if x == n-1 and y == n-1:
            return cnt

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                visited[nx][ny] = visited_num
                heapq.heappush(pq,(cnt+board[nx][ny],-nx,-ny))
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif visited[x][y] == visited_num:
        return False
    return True
for t in range(1,tc+1):
    visited_num += 1
    solv(t)