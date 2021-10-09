from sys import stdin
input = stdin.readline

tc = int(input())
def solv():
    for _ in range(tc):
        n = int(input())
        student = [0]+list(map(int, input().split()))
        visited = [0]*(n+1)
        team = [False]*(n+1)
        ans = n
        for start in range(1,n+1):
            if not team[start] and visited[start] == 0:
                ans -= check_team(student,visited,start,team)
        print(ans)

def check_team(student,visited,start,team):
    now = student[start]
    path = [start]
    while True:
        nxt = student[now]
        if team[nxt]:
            return 0
        if visited[nxt] == start:
            flag = False
            cnt = 0
            for p in path:
                if p == nxt:
                    flag = True
                if flag:
                    team[p] = True
                    cnt += 1
            return cnt

        if nxt == start:
            for p in path:
                team[p] = True
            return len(path)
        if now == nxt:
            return 0
        path.append(nxt)
        now = student[nxt]
        if visited[nxt] != 0:
            return 0
        visited[nxt] = start

solv()