from sys import stdin
input = stdin.readline
class Node:
    def __init__(self,alpha):
        self.alpha = alpha
        self.child = []
        self.is_end = False
        self.count = 0
def solv():
    global total
    while True:
        total = 0
        n,words = input_data()
        if n == -1:
            break

        tri = make_tri(words)
        travel_tri(tri,0)
        print('%.2f'%round(total/n,2))

def travel_tri(now, count):
    global total
    if now.is_end:
        total += count
    elif now.count == 1:
        total += count
        return

    if not now.is_end and len(now.child) == 1:
        if now.alpha == '-':
            travel_tri(now.child[0], count+1)
        else:
            travel_tri(now.child[0], count)
    else:
        for child in now.child:
            travel_tri(child, count + 1)


def make_tri(words):
    tri = Node('-')

    for word in words:
        now = tri
        for alpha in word:
            now = search_child(now, alpha)
        now.is_end = True

    return tri


def search_child(now, target):
    for child in now.child:
        if child.alpha == target:
            child.count += 1
            return child
    node = Node(target)
    node.count = 1
    now.child.append(node)
    return node
def input_data():
    try:
        n = int(input())
        words = [input().strip() for _ in range(n)]
        return n,words
    except:
        return -1,[]
solv()