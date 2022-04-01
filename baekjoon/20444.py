n,k = map(int, input().split())

def solv():
    left = 0
    right = n

    while left <= right:
        r = (left+right)//2
        c = n-r

        cnt = (r+1)*(c+1)
        if cnt == k:
            print('YES')
            return
        elif cnt < k:
            left = r + 1
        else:
            right = r - 1
    print('NO')
solv()