import sys
from itertools import permutations

n = int(sys.stdin.readline())
price_map = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def calc_total_price(visit_order_list, sum):
    if price_map[visit_order_list[n-1]][0] == 0:
        return 2100000000

    for i in range(0,n-1):
        from_spot  = visit_order_list[i]
        to_spot = visit_order_list[i+1]

        if price_map[from_spot][to_spot] != 0:
            sum += price_map[from_spot][to_spot]
        else:
            return 2100000000
    sum += price_map[visit_order_list[n-1]][0]
    return sum

permu_list = permutations([i for i in range(1,n)],n-1)

ans = 2100000000

for permu in permu_list:
    visit_order_list = list(permu)
    visit_order_list.insert(0,0)
    ans = min(ans, calc_total_price(visit_order_list, 0))

print(ans)