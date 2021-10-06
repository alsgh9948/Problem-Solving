from itertools import combinations
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
board = [list(input()) for _ in range(5)]

def solv():
    ans = 0
    select = [[False]*5 for _ in range(5)]
    visited = [[0]*5 for _ in range(5)]
    num = 1
    for comb in combinations([i for i in range(25)], 7):
        p_list = []
        cnt = 0
        for p in comb:
            x = p//5
            y = p%5
            if board[x][y] == 'S':
                cnt += 1
            p_list.append((x,y))
            select[x][y] = True
        if cnt >= 4:
            q = deque([p_list[0]])
            visited[p_list[0][0]][p_list[0][1]] = num

            tmp_cnt = 0
            while q:
                x,y = q.pop()
                tmp_cnt += 1

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if point_validator(nx,ny) and select[nx][ny] and visited[nx][ny] != num:
                        visited[nx][ny] = num
                        q.appendleft((nx,ny))
            if tmp_cnt == 7:
                ans += 1
        for x,y in p_list:
            select[x][y] = False
        num += 1
    print(ans)
def point_validator(x,y):
    if x < 0 or y < 0 or x >= 5 or y >= 5:
        return False
    return True

solv()

