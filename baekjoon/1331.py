def solv():
    cnt = 0
    visited = [[False]*6 for _ in range(6)]
    start,end,pos='','',''
    before = ''
    for _ in range(36):
        pos = input()
        x,y = trans_pos(pos)
        if not start:
            start = pos
        if visited[x][y]:
            break
        elif before and not is_movable(before,pos):
            break
        else:
            cnt += 1
            visited[x][y] = True
        before = pos
    end = pos

    if cnt == 36:
        if is_movable(start,end):
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')

def is_movable(before,now):
    bx,by = trans_pos(before)
    nx,ny = trans_pos(now)
    if (abs(bx-nx) == 2 and abs(by-ny) == 1) or (abs(bx-nx) == 1 and abs(by-ny) == 2):
        return True
    else:
        return False
def trans_pos(pos):
    x = 6-int(pos[1])
    y = ord('F')-ord(pos[0])
    return x,y
solv()