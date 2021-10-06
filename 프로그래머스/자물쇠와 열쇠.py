def solution(k, l):
    global m, n, key, lock, empty_cnt
    key = k
    lock = l
    m = len(key)
    n = len(lock)
    empty_cnt = 0

    for row in lock:
        empty_cnt += row.count(0)

    for _ in range(4):
        if move_key():
            return True
        key = rotate_key(key)

    return False


def move_key():
    sx = sy = 1 - m
    ex = ey = n
    for x in range(sx, ex):
        for y in range(sy, ey):
            if check_key(x, y):
                return True
    return False


def check_key(sx, sy):
    cnt = 0
    kx = -1
    for x in range(sx, sx + m):
        kx += 1
        if x < 0:
            continue
        elif x >= n:
            break
        ky = -1
        for y in range(sy, sy + m):
            ky += 1
            if y < 0:
                continue
            elif y >= n:
                break
            if lock[x][y] == 0 and key[kx][ky] == 1:
                cnt += 1
            elif lock[x][y]==key[kx][ky]:
                return False
    if cnt == empty_cnt:
        return True
    return False


def rotate_key(key):
    tmp = [[0] * m for _ in range(m)]

    for x in range(m):
        for y in range(m):
            tmp[y][m - x - 1] = key[x][y]

    return tmp

a = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
b = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(a,b))