from collections import deque

n,k = map(int,input().strip().split())

board = [[False,False] for _ in range(500001)]

def solv():
    global board, k

    q = deque()
    q.appendleft((n,0))

    board[n][0] = True
    t = 0
    while q:
        k += t

        if k > 500000:
            return -1

        q_len = len(q)

        for _ in range(q_len):
            now,cnt = q.pop()

            if now == k or board[k][cnt%2]:
                return t
            if now+1 <= 500000 and not board[now+1][(cnt+1)%2]:
                q.appendleft((now+1,cnt+1))
                board[now+1][(cnt+1)%2] = True

            if now-1 >= 0 and not board[now-1][(cnt+1)%2]:
                q.appendleft((now-1,cnt+1))
                board[now-1][(cnt+1)%2] = True

            if now*2 <= 500000 and not board[now*2][(cnt+1)%2]:
                q.appendleft((now*2,cnt+1))
                board[now*2][(cnt+1)%2] = True

        t += 1

    return -1
print(solv())