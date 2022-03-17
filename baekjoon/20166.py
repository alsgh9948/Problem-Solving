from sys import stdin
from collections import defaultdict, deque

input = stdin.readline
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

n,m,k = map(int, input().split())
board = [input().strip() for _ in range(n)]

targets = [input().strip() for _ in range(k)]

words = defaultdict(int)
def solv():
    set_words()
    for target in targets:
        print(words[target])

def set_words():
    for sx in range(n):
        for sy in range(m):
            bfs(sx,sy)
def bfs(sx,sy):
    global words

    q = deque([(sx,sy,board[sx][sy])])
    words[board[sx][sy]] += 1

    while q:
        x,y,word = q.pop()

        for d in range(8):
            nx = (x + dx[d])%n
            ny = (y + dy[d])%m

            new_word = word + board[nx][ny]
            len_new_word = len(new_word)
            words[new_word] += 1

            if len_new_word < 5:
                q.appendleft((nx,ny,new_word))

solv()