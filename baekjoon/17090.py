from sys import stdin

input = stdin.readline
dir = {
    'U':(-1,0),
    'D':(1,0),
    'L':(0,-1),
    'R':(0,1)
}

n,m = map(int, input().split())
board = [input().strip() for _ in range(n)]
visited = [[0]*m for _ in range(n)]
visited_num = 0

is_possible = [[-1]*m for _ in range(n)]

def solv():
    global visited_num
    answer = 0
    for sx in range(n):
        for sy in range(m):
            if is_possible[sx][sy] == -1:
                visited_num += 1
                answer += simul(sx,sy)
            else:
                answer += is_possible[sx][sy]
    print(answer)
def simul(x,y):
    global visited, is_possible

    s = [(x,y)]
    rst = -1
    while True:
        visited[x][y] = visited_num

        d = board[x][y]
        x += dir[d][0]
        y += dir[d][1]


        if not boundary_validator(x, y):
            rst = 1
            break
        else:
            s.append((x,y))
            if is_possible[x][y] != -1:
                rst = is_possible[x][y]
                break
            else:
                if visited[x][y] == visited_num:
                    rst = 0
                    break
    for x,y in s:
        is_possible[x][y] = rst
    return rst
def boundary_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True

solv()