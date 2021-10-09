dx = [0,-1,0,1]
dy = [1,0,-1,0]

r1,c1,r2,c2 = map(int, input().split())
r1 += 5000
c1 += 5000
r2 += 5000
c2 += 5000

board = [['0']*5 for _ in range(50)]

def set_board():
    global board
    x,y = 5000,5000
    max_length = 0
    num_cnt = 0
    d = 0
    rotate_cnt = 0
    cnt = 0
    max_cnt = 1
    num = 1
    while True:
        if r1 <= x <= r2 and c1 <= y <= c2:
            board[x-r1][y-c1] = str(num)
            max_length = max(len(str(num)), max_length)
            num_cnt += 1

            if num_cnt == (r2-r1+1)*(c2-c1+1):
                return max_length
        num += 1
        x += dx[d]
        y += dy[d]
        cnt += 1

        if cnt == max_cnt:
            d = (d+1)%4
            cnt = 0

            rotate_cnt += 1

            if rotate_cnt == 2:
                rotate_cnt = 0
                max_cnt += 1

def solv():
    max_length = set_board()
    for x in range(r2-r1+1):
        for y in range(c2-c1+1):
            print_num = ' '*(max_length-len(board[x][y]))+board[x][y]
            print(print_num,end=' ')
        print()
solv()