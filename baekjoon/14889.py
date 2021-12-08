from sys import stdin
from itertools import combinations

input = stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def solv():
    answer = 9876543210

    for start_team in combinations(range(1,n),n//2-1):
        start_team = list(start_team)+[0]
        link_team = [i for i in range(n) if i not in start_team]

        start_status = calc_status(start_team)
        link_status = calc_status(link_team)

        answer = min(answer,(abs(start_status-link_status)))
    print(answer)

def calc_status(team):
    status = 0
    for i in range(n//2):
        a = team[i]
        for j in range(i+1,n//2):
            b = team[j]
            status += board[a][b] + board[b][a]
    return status
solv()