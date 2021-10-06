from sys import stdin
dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,1,-1,-1,1]

n,m,k = map(int,stdin.readline().strip().split())

a = []
land_map = [[[5,[]] for _ in range(n)] for _ in range(n)]
extend_tree_map = [[0]*(n) for _ in range(n)]

for i in range(n):
    a.append(list(map(int,stdin.readline().strip().split())))

for _ in range(m):
    x, y, z = map(int, stdin.readline().strip().split())

    land_map[x-1][y-1][1].append(z)

def solv():

    for _ in range(k):
        spring_summer()
        fall_winter()

    ans = 0
    for i in range(n):
        for j in range(n):
           ans += len(land_map[i][j][1])
    return ans

def spring_summer():
    global a, land_map, extend_tree_map
    for i in range(n):
        for j in range(n):
            trees = land_map[i][j][1]
            new_tree = []
            trees.sort()
            add_a = 0
            for age in trees:
                if land_map[i][j][0] >= age:
                    new_age = age + 1
                    new_tree.append(new_age)
                    land_map[i][j][0] -= age

                    if new_age%5 == 0:
                        extend_tree_map[i][j] += 1
                else:
                    add_a += age//2
            land_map[i][j][1] = new_tree
            land_map[i][j][0] += add_a

def fall_winter():
    global land_map, extend_tree_map
    for i in range(n):
        for j in range(n):
            land_map[i][j][0] += a[i][j]
            if extend_tree_map[i][j] > 0:
                for d in range(8):
                    nx = i + dx[d]
                    ny = j + dy[d]

                    if not point_validator(nx,ny):
                        continue
                    for _ in range(extend_tree_map[i][j]):
                        land_map[nx][ny][1].append(1)
                extend_tree_map[i][j] = 0

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True

print(solv())