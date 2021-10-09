from sys import stdin

input = stdin.readline
n = int(input())

graph = [[987654321]*n for _ in range(n)]
while True:
    a,b = map(int, input().split())
    if a == -1:
        break
    graph[a-1][b-1] = graph[b-1][a-1] = 1

def solv():
    global graph
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j:
                    graph[i][j] = 0
                elif graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    ans_score=98765431
    ans_cnt=0
    ans_list=[]
    for i in range(n):
        score = max(graph[i])
        if score != 0:
            if score == ans_score:
                ans_cnt += 1
                ans_list.append(i+1)
            elif score < ans_score:
                ans_cnt = 1
                ans_list = [i+1]
                ans_score = score

    print(ans_score,ans_cnt)
    print(*ans_list)

solv()