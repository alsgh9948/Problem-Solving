from sys import stdin

input = stdin.readline

n,m = map(int, input().split())
group = [i for i in range(n+1)]

true_list = set(list(map(int, input().split()))[1:])

parties = [list(map(lambda x:int(x), input().split()))[1:] for _ in range(m)]

def solv():
    set_group()

    answer = 0
    for party in parties:
        for idx in party:
            if find(group[idx]) in true_list:
                break
        else:
            answer += 1
    print(answer)

def set_group():
    global group

    for party in parties:
        for idx in range(len(party)-1):
            union(party[idx],party[idx+1])
def find(target):
    global group

    if group[target] == target:
        return target

    group[target] = find(group[target])
    return group[target]

def union(a,b):
    global group,true_list

    a = find(a)
    b = find(b)

    if a != b:
        group[a] = b
        if a in true_list or b in true_list:
            true_list.add(a)
            true_list.add(b)
solv()