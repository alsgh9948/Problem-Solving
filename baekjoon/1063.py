from sys import stdin

input = stdin.readline
dir = {
    'R': (0, 1),
    'L': (0,-1),
    'T': (1,0),
    'B': (-1, 0),
    'RT': (1,1),
    'LT': (1,-1),
    'RB': (-1, 1),
    'LB': (-1,-1),
}
kp,sp,n = input().split()

king = (int(kp[1])-1,ord(kp[0])-ord('A'))
stone = (int(sp[1])-1,ord(sp[0])-ord('A'))

def solv():
    global king, stone
    for _ in range(int(n)):
        op = input().strip()

        kx,ky = king
        knx = kx + dir[op][0]
        kny = ky + dir[op][1]

        if point_validator(knx,kny):
            sx,sy = stone
            if knx == sx and kny == sy:
                snx = sx + dir[op][0]
                sny = sy + dir[op][1]

                if point_validator(snx,sny):
                    stone = (snx,sny)
                else:
                    continue
            king = (knx, kny)

    print(chr(king[1]+ord('A'))+''+str(king[0]+1))
    print(chr(stone[1]+ord('A'))+''+str(stone[0]+1))
def point_validator(x,y):
    if x < 0 or y < 0 or x >= 8 or y >= 8:
        return False
    return True

solv()