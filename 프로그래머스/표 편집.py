def solution(n, k, cmds):
    answer = ['O'] * n
    head, tail, now = set_list(n, k)

    tmp = []
    for cmd in cmds:
        if cmd == 'C':
            answer[now.num] = 'X'
            tmp.append(now)
            if now.down and now.up:
                now.up.down = now.down
                now.down.up = now.up
                now = now.down
            elif not now.down:
                now.up.down = None
                now = now.up
                tail = now
            else:
                now.down.up = None
                now = now.down
                head = now
        elif cmd == 'Z':
            target = tmp.pop()
            if tail.num < target.num:
                tail.down = target
                target.up = tail
                tail = target
            elif head.num > target.num:
                head.up = target
                target.down = head
                head = target
            else:
                up = search_node(target,-1,answer)
                down = search_node(target,1,answer)

                target.up = up
                up.down = target
                target.down = down
                down.up = target

            answer[target.num] = 'O'
        else:
            order, x = cmd.split()
            x = int(x)
            if order == 'U':
                for _ in range(x):
                    now = now.up
            else:
                for _ in range(x):
                    now = now.down
    return ''.join(answer)

def search_node(node,dir,answer):
    while node and answer[node.num] == 'X':
        if dir == 1:
            node = node.down
        else:
            node = node.up
    return node

class Node(object):
    def __init__(self, num):
        self.num = num
        self.up = None
        self.down = None

def set_list(n, k):
    target = None

    head = None
    now = head
    for num in range(n):
        node = Node(num)
        if not now:
            head = node
            now = head
        else:
            now.down = node
            node.up = now
            now = now.down
        if num == k:
            target = now
    tail = now
    return head, tail, target
a = 8
b = 2
c = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
print(solution(a,b,c))