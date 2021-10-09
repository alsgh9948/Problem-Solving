from collections import deque

t = int(input())

def bfs(a,b):
    ans = 0
    q = deque()

    visited = [None]*10000
    q.appendleft(a)

    visited[a] = ('',-1)

    while q:
        now = q.pop()
        if now == b:
            cmd, now = visited[b]
            ans = deque()
            while now != -1:
                ans.appendleft(cmd)
                cmd, now = visited[now]
            return ans
        for c in ('D','S','L','R'):
            next_num = command(c,now)
            if visited[next_num]: continue
            visited[next_num] = (c,now)
            q.appendleft(next_num)

    return ans

def command(c, num):
    if c == 'D':
        return (num*2)%10000
    elif c == 'S':
        return num-1 if num > 0 else 9999
    elif c == 'L':
        return num%1000*10+num//1000
    elif c == 'R':
        return num//10+num%10*1000
for _ in range(t):
    a,b = map(int,input().split())
    ans = bfs(a,b)
    for c in ans:
        print(c,end='')
    print()
