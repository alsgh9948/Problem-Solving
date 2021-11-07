from sys import stdin
input = stdin.readline
class Node:
    def __init__(self,alpha):
        self.alpha = alpha
        self.child = []
        self.is_word = False

def solv():
    global total
    while True:
        total = 0
        n,words = input_data()
        if n == -1:
            break

        tri = make_tri(words)
        for start in tri.child:
            simul(start,1)
        print('%.2f'%round(total/n,2))
def simul(now,count):
    global total
    if now.is_word:
        total += count
    if now.child:
        if not now.is_word and len(now.child) == 1:
            simul(now.child[0],count)
        else:
            for nxt in now.child:
                simul(nxt,count+1)
def make_tri(words):
    tri = Node('-')
    now = tri
    for word in words:
        for alpha in word:
            now = search_child(now,alpha)
        now.is_word = True
        now = tri
    return tri
def search_child(now, target):
    for child in now.child:
        if child.alpha == target:
            return child
    node = Node(target)
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