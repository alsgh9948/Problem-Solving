n = int(input())

num_list = []
def solv():
    for start in range(10):
        search_num(start,start-1)

    if n >= len(num_list):
        print(-1)
    else:
        num_list.sort()
        print(num_list[n])
def search_num(num,now):
    global count
    num_list.append(num)
    if now == -1:
        return
    for nxt in range(now,-1,-1):
        search_num(num*10+nxt,nxt-1)
solv()