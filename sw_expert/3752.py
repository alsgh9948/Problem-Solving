tc = int(input())

visited = [0]*10001
visited_num = 0
def solv(t):
    global visited
    n = int(input())
    nums = list(map(int, input().split()))
    max_num = sum(nums)

    visited[0] = visited_num
    for num in nums:
        for idx in range(max_num,-1,-1):
            if visited[idx] == visited_num:
                visited[idx+num] = visited_num
    print('#%d %d'%(t, visited.count(visited_num)))
for t in range(1,tc+1):
    visited_num += 1
    solv(t)