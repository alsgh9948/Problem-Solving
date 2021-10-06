n = int(input())
s = input()

_map = [[0]*n for _ in range(n)]
temp_idx = 0
for i in range(n):
    for j in range(i,n):
        _map[i][j] = s[temp_idx]
        temp_idx+=1
def check_sum(idx,select_list):
    sum = 0
    for i in range(idx,-1,-1):
        sum += select_list[i]
        if sum > 0 and _map[i][idx] != '+': return False
        if sum == 0 and _map[i][idx] != '0': return False
        if sum < 0 and _map[i][idx] != '-': return False
    return True

def select_num(cnt,select_list):
    if cnt == n:
            print(*select_list)
            return True
    for i in range(-10,11):
            select_list.append(i)
            if check_sum(cnt,select_list):
                if select_num(cnt+1,select_list):
                    return True
            select_list.pop()
    return False

select_num(0,[])