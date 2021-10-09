tc = int(input())

def solv(t):
    global n,m,board
    n,m = map(int, input().split())
    board = []
    homes = []
    for x in range(n):
        board.append(list(map(int, input().split())))
        for y in range(n):
            if board[x][y] == 1:
                homes.append((x,y))

    k = 1
    answer = 0
    while True:
        operating_price = k*k+(k-1)*(k-1)
        if len(homes)*m - operating_price < 0:
            break
        for x in range(n):
            for y in range(n):
                cnt = 0
                for home in homes:
                    distance = calc_distance(x,y,home)
                    if distance <= k-1:
                       cnt += 1
                if cnt*m - operating_price >= 0:
                    answer = max(answer,cnt)
        k += 1
    print('#%d %d'%(t,answer))
def calc_distance(x,y,home):
    return abs(x-home[0])+abs(y-home[1])
for t in range(1,tc+1):
    solv(t)