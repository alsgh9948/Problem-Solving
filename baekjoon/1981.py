from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())

board = []
num_list = set()
for x in range(n):
    board.append(list(map(int, input().split())))
    for num in board[x]:
        num_list.add(num)

num_list = sorted(list(num_list))
visited = [[0]*n for _ in range(n)]
visited_num = 0
def solv():
    low=high=0
    answer = 9876543210

    while low < len(num_list) and high < len(num_list):
        if bfs(num_list[low],num_list[high]):
            if low == high:
                print(0)
                return
            else:
                answer = min(answer, abs(num_list[high]-num_list[low]))
                low += 1
        else:
            high += 1
    print(answer)
def bfs(low,high):
    global visited,visited_num
    if board[0][0] < low or board[0][0] > high:
        return False
    visited_num += 1
    visited[0][0] = visited_num
    q = deque([(0,0)])
    while q:
        x,y = q.pop()

        if x == n-1 and y == n-1:
            return True
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                if low <= board[nx][ny] <= high:
                    visited[nx][ny] = visited_num
                    q.appendleft((nx,ny))
    return False
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif visited[x][y] == visited_num:
        return False
    return True

solv()