from itertools import combinations

dx = [-1,1,0,0]
dy = [0,0,-1,1]
n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
flower_board = [[False]*n for _ in range(n)]

nums = [i for i in range(n*n)]
def solv():
    ans = 987654321
    for comb in combinations(nums,3):
       total = 0
       flag = True
       for num in comb:
           tmp = set_flower(num,True)
           if tmp >= 0:
               total += tmp
           else:
               flag = False
               break
       if flag:
           ans = min(ans,total)
       for num in comb:
            set_flower(num,False)
    print(ans)

def set_flower(num, typ):
    global flower_board

    x = num//n
    y = num%n
    total = board[x][y]
    if x == 0 or y == 0 or x == n-1 or y == n-1:
        return -1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if typ and flower_board[nx][ny]:
            return -1
        total += board[nx][ny]
        flower_board[nx][ny] = typ

    flower_board[x][y] = typ
    return total

solv()