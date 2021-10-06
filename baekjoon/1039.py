n,k = input().split()
k = int(k)

def solv():
    global n
    if int(n) < 10 or (int(n) < 100 and int(n)%10==0):
        print(-1)
    else:
        n = list(n)
        idx_list = set_idx_list(n)

        order = sorted(n,reverse=True)
        idx = 0
        for _ in range(k):
            if idx >= len(n)-1:
                n[-1],n[-2] = n[-2],n[-1]
            else:
                target = int(order[idx])
                if n[idx] == target:
                    continue
                else:
                    if min(n[idx:]) == n[idx]:
                        target_idx = idx_list[target][-1]
                        idx_list[target][-1] = -1
                    else:
                        target_idx = search_target(idx_list,target)
                    n[idx],n[target_idx] = n[target_idx],n[idx]

                    change_idx(idx_list,int(n[target_idx]),idx,target_idx)
            idx += 1
        print(''.join(n))

def search_target(idx_list,target):
    for i in range(len(idx_list[target])):
        if idx_list[target][i] != -1:
            ret = idx_list[target][i]
            idx_list[target][i] = -1
            return ret
def set_idx_list(n):
    idx_list = [[] for _ in range(10)]
    for idx in range(len(n)):
        idx_list[int(n[idx])].append(idx)

    for idx in range(10):
        idx_list[idx].sort()

    return idx_list
def change_idx(idx_list, target, idx,target_idx):
    for i in range(len(idx_list[target])):
        if idx_list[target][i] == idx:
            idx_list[target][i] = target_idx
            return

solv()