n,k = map(int, input().split())

def solv():
    cnt = 9
    length = 2
    op = 90
    before = 0
    while length <= 10**9:
        if n > cnt:
            before = cnt
            cnt += length*op
            length += 1
            op *= 10
        else:
            break

    left = before
    right = cnt
    print(-1)

solv()