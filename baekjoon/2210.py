dx = [-1,1,0,0]
dy = [0,0,-1,1]

board = [input().strip().split() for _ in range(5)]

ans = set([])
def solv():
    for i in range(5):
        for j in range(5):
           dfs(i,j,0,[0,0,0,0,0,0])

def dfs(x,y,cnt,num_list):
    if cnt == 6:
        num_str = ''
        for num in num_list:
            num_str += num
        global ans
        ans.add(num_str)
        return

    num_list[cnt] = board[x][y]
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if not point_validator(nx,ny):
            continue
        dfs(nx,ny,cnt+1,num_list)
def point_validator(x,y):
    if x < 0 or y < 0 or x >= 5 or y >= 5:
        return False
    return True

solv()
print(len(ans))