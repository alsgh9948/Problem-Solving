dx = [1,-1,0,0]
dy = [0,0,-1,1]
MAX = 4001
tc = int(input())

board = [[0]*MAX for _ in range(MAX)]
visited_num = 1
def solv(t):
    global board, visited_num, atoms
    atoms = []
    n = int(input())
    visited_num += 1
    for _ in range(n):
        y,x,d,k = map(int, input().split())
        x = (x+1000)*2
        y = (y+1000)*2
        board[x][y] = visited_num
        atoms.append([x,y,d,k])
    print('#%d %d'%(t,simul()))
def simul():
    global visited_num
    answer = 0
    cnt = 0
    while cnt < len(atoms):
        visited_num += 1
        tmp_cnt, remove_atoms_points = move_atoms()
        cnt += tmp_cnt
        if remove_atoms_points:
            tmp_cnt, tmp_sum = remove_atoms(remove_atoms_points)
            answer += tmp_sum
            cnt += tmp_cnt
    return answer

def move_atoms():
    global board, atoms
    remove_atoms_points = []
    cnt = 0
    for idx in range(len(atoms)):
        x,y,d,k = atoms[idx]
        if k == -1:
            continue
        x += dx[d]
        y += dy[d]

        if point_validator(x,y):
            if abs(board[x][y]) == visited_num:
                if board[x][y] > 0:
                    remove_atoms_points.append((x,y))
                    board[x][y] *= -1
            else:
                board[x][y] = visited_num
            atoms[idx] = [x,y,d,k]
        else:
            atoms[idx][3] = -1
            cnt += 1
    return cnt, remove_atoms_points

def remove_atoms(remove_atoms_points):
    global board, atoms
    answer = 0
    cnt = 0
    for x,y in remove_atoms_points:
        for idx in range(len(atoms)):
            ax,ay,d,k = atoms[idx]
            if k == -1:
                continue
            if x == ax and y == ay:
                answer += k
                cnt += 1
                atoms[idx][3] = -1
    return cnt, answer
def point_validator(x,y):
    if x < 0 or y < 0 or x >= MAX or y >= MAX:
        return False
    return True
for t in range(1, tc+1):
    solv(t)