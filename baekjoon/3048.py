n,m = map(int, input().split())

n1 = list(input())
n2 = input()
n1.reverse()

arr = []
for c in n1:
    arr.append([c,0,0])
for c in n2:
    arr.append([c,1,0])

t = int(input())

if t >= n+m-1:
    print(n2+''.join(n1))
else:
    for _ in range(t):
        idx = 0
        while idx+1 < n+m:
            if (arr[idx][1] == 0 and arr[idx][2] == m) or (arr[idx][1] == 1 and arr[idx][2] == n):
                idx+= 1
            elif arr[idx][1] != arr[idx+1][1]:
                arr[idx],arr[idx+1] = arr[idx+1],arr[idx]
                arr[idx][2] += 1
                arr[idx+1][2] += 1
                idx += 2
            else:
                idx += 1
    for c,typ,cnt in arr:
        print(c,end='')