from sys import stdin

input = stdin.readline
n = int(input())
a_list = list(map(int, input().split()))
visited = [0] * (n)
visited_num = 0

def solv():
    global visited_num
    left = 1
    right = 1000000*5000

    while left <= right:
        mid = (left+right)//2
        visited_num += 1

        if is_possible(mid):
            right = mid-1
        else:
            left = mid+1
    print(left)

def is_possible(power):
    global visited
    s = [0]
    while s:
        now = s.pop()
        for nxt in range(now+1,n):
            required_power = (nxt-now)*(1+abs(a_list[now]-a_list[nxt]))
            if visited[nxt] != visited_num and required_power <= power:
                if nxt == n-1:
                    return True
                visited[nxt] = visited_num
                s.append(nxt)
    return False

solv()
