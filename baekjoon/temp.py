import sys
def go(cnt,arr):
    global n,m,num_arr
    if cnt==m:
        print(*arr)
        return
        # for i in range(m):
        #     if i==m-1:
        #         print(arr[i],end='\n')
        #         return
        #     print(arr[i],end=' ')
    for i in range(0,n):
        print(num_arr[0])
        arr.append(num_arr[i])
        go(cnt+1,arr)
        arr.pop()

n,m=map(int,sys.stdin.readline().split())
num_arr=list(map(int,sys.stdin.readline().split()))
num_arr.sort()
arr=[]
go(0,arr)