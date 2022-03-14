from sys import stdin

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())

board = []
visited_board = [[False]*m for _ in range(n)]
target_count = 0

for x in range(n):
    board.append(input())
    for y in range(m):
        if board[x][y] == '*':
            target_count += 1

def solv():
    max_size = min(n,m)//2 + (0 if min(n,m)%2 == 0 else 1)
    answer = []
    for x in range(n):
        for y in range(m):
            if board[x][y] == '*':
                for size in range(max_size,0,-1):
                    if is_possible_insert_cross(x,y,size):
                        answer.append((x+1,y+1,size))
                        break

    if target_count == 0:
        print(len(answer))
        for ans in answer:
            print(*ans)
    else:
        print(-1)
    return False

def is_possible_insert_cross(x,y,size):
    global visited_board, target_count

    visited_list = []
    if not visited_board[x][y]:
        visited_list.append((x,y))
    for d in range(4):
        nx, ny = x, y
        for _ in range(size):
            nx += dx[d]
            ny += dy[d]

            if not point_validator(nx,ny):
                return False

            if not visited_board[nx][ny]:
                visited_list.append((nx,ny))

    for nx,ny in visited_list:
        visited_board[nx][ny] = True
        target_count -= 1
    return True

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == '.':
        return False
    return True
solv()