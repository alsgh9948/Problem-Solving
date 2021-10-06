from sys import stdin

input = stdin.readline

n,k = map(int,input().split())

convair = []
cnts = list(map(int,input().split()))
for cnt in cnts:
    convair.append([False,cnt])

def solv():
    cnt = 0
    ans = 0
    while True:
        ans += 1
        rotate_convair()
        cnt += rotate_robots()
        cnt += add_robot()
        if cnt >= k:
            return ans

def rotate_convair():
    global convair

    convair[n-1][0] = False
    tmp = convair[-1]
    for idx in range(n*2-1,0,-1):
        convair[idx] = convair[idx-1]
    convair[0] = tmp
    convair[n-1][0] = False

def rotate_robots():
    global convair
    cnt = 0
    for now in range(n*2-1,-1,-1):
        if not convair[now][0]:
            continue

        nxt = (now+1)%(n*2)

        if point_validator(nxt):
            convair[now][0] = False
            convair[nxt][1] -= 1

            if convair[nxt][1] == 0:
                cnt += 1

            if convair != n-1:
                convair[nxt][0] = True

    return cnt

def add_robot():
    global convair

    if convair[0][1] > 0:
        convair[0][0] = True
        convair[0][1] -= 1

        if convair[0][1] == 0:
            return 1
    return 0

def point_validator(nxt):
    if convair[nxt][0]:
        return False
    elif convair[nxt][1] == 0:
        return False
    return True

print(solv())