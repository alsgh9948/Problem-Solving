from sys import stdin

n,l = map(int, stdin.readline().strip().split())

board = [list(map(int, stdin.readline().strip().split())) for _ in range(n)]

def check_slope(x,y,d,h,slope):

    if d == 0:
        if x-l+1 < 0:
            return False
        cnt = 0
        for nx in range(x,x-l,-1):
            if not point_validator(nx,y,nx,h,slope):
                return False
            cnt += 1
            if cnt == l:
                set_slope(x-l+1, x+1, slope)
                return True

    elif d == 1:
        if x+l > n:
            return False
        cnt = 0
        for nx in range(x,x+l):
            if not point_validator(nx,y,nx,h,slope):
                return False
            cnt += 1
            if cnt == l:
                set_slope(x, x+l, slope)
                return True

    elif d == 2:
        if y-l+1 < 0:
            return False
        cnt = 0
        for ny in range(y,y-l,-1):
            if not point_validator(x,ny,ny,h,slope):
                return False
            cnt += 1
            if cnt == l:
                set_slope(y-l+1, y+1, slope)
                return True

    elif d == 3:
        if y+l > n:
            return False
        cnt = 0
        for ny in range(y,y+l):
            if not point_validator(x,ny,ny,h,slope):
                return False
            cnt += 1
            if cnt == l:
                set_slope(y, y+l, slope)
                return True
def set_slope(start,end,slope):
    for i in range(start,end):
        slope[i] = True

def point_validator(x,y,si,h,slopes):
    if board[x][y] != h:
        return False
    elif slopes[si]:
        return False
    return True

def row_check():
    row_cnt = 0
    slopes = [[False]*n for _ in range(n)]
    for i in range(n):
        j = 0
        while j < n-1:
            if board[i][j] < board[i][j+1]:
                if abs(board[i][j] - board[i][j+1]) != 1:
                    break
                elif check_slope(i, j, 2, board[i][j], slopes[i]):
                    pass
                else:
                    break
            elif board[i][j] > board[i][j+1]:
                if abs(board[i][j] - board[i][j+1]) != 1:
                    break
                elif check_slope(i, j+1, 3, board[i][j+1], slopes[i]):
                    j+=l-1
                else:
                    break
            j+=1
        if j >= n-1:
            row_cnt+=1
    return row_cnt
def cul_check():
    cul_cnt = 0
    slopes = [[False]*n for _ in range(n)]
    for j in range(n):
        i = 0
        while i < n-1:
            if board[i][j] < board[i+1][j]:
                if abs(board[i][j] - board[i+1][j]) != 1:
                    break
                elif check_slope(i, j, 0, board[i][j], slopes[j]):
                    pass
                else:
                    break
            elif board[i][j] > board[i+1][j]:
                if abs(board[i][j] - board[i+1][j]) != 1:
                    break
                elif check_slope(i+1, j, 1, board[i+1][j], slopes[j]):
                    i+=l-1
                else:
                    break
            i+=1
        if i >= n-1:
            cul_cnt+=1
    return cul_cnt

print(row_check()+cul_check())